<template>
	<div class="fixed z-10 inset-0 overflow-y-auto">
		<div
			class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
		>
			<div class="fixed inset-0 transition-opacity">
				<div class="absolute inset-0 bg-gray-500 opacity-75"></div>
			</div>
			<div
				class="w-2/3 inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8"
				role="dialog"
				aria-modal="true"
				aria-labelledby="modal-headline"
			>
				<div
					class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4 w-2/3 mx-auto"
				>
					<div class="flex justify-between">
						<div
							class="text-gray-600 uppercase tracking-wide text-xs font-bold"
						>
							<a
								:href="`https://${mark.website}`"
								target="_blank"
								v-if="mark.website"
								class="p-2 bg-gray-200 rounded flex items-center"
								content="Open Website Home"
								v-tippy
							>
								<img
									v-if="mark.favicon"
									:src="mark.favicon"
									class="inline-block h-4 mr-2"
								/>
								{{ mark.website }}
							</a>
						</div>
						<div class="flex justify-end">
							<a
								:href="mark.url"
								target="_blank"
								class="text-gray-400 mr-4 hover:text-teal-500 focus:outline-none cursor-pointer"
								content="Open Article Link"
								v-tippy
							>
								<unicon
									name="external-link-alt"
									fill="currentColor"
									height="18"
									width="18"
								/>
							</a>
							<a
								target="_blank"
								class="text-gray-400 mr-4 hover:text-red-500 focus:outline-none cursor-pointer"
								:content="deleteTipContent"
								@click="deleteMark"
								v-tippy="{
									hideOnClick: false,
								}"
							>
								<unicon
									name="trash-alt"
									fill="currentColor"
									height="18"
									width="18"
								/>
							</a>
							<a
								target="_blank"
								class="text-gray-400 mr-4 hover:text-gray-800 focus:outline-none cursor-pointer"
								content="Close Article"
								@click.prevent="closeModal"
								v-tippy
							>
								<unicon
									name="times"
									fill="currentColor"
									height="18"
									width="18"
								/>
							</a>
						</div>
					</div>
					<div class="prose prose-md my-12">
						<h2
							class="text-2xl leading-6 font-medium text-gray-900"
							id="modal-headline"
						>
							{{ mark.meta_title }}
						</h2>
						<div class="mt-2 overflow-scroll limit-height">
							<div v-html="mark.readable"></div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "ArticlePreview",
	props: ["mark"],
	data() {
		return {
			deleteConfirm: false,
			deleteTipContent: "Delete Article",
		};
	},
	created() {
		document.addEventListener("keyup", this.onClose);
	},
	destroyed() {
		document.removeEventListener("keyup", this.onClose);
	},
	methods: {
		closeModal() {
			this.$emit("close");
		},
		deleteMark() {
			if (this.deleteConfirm) {
				this.$call("delete_mark", {
					mark: this.mark.name,
				}).then(() => {
					this.closeModal();
					this.$eventHub.$emit("updated-links");
				});
			} else {
				this.deleteTipContent = "Click Again to Confirm";
				this.deleteConfirm = true;
				// this.deleteTipTrigger = "mouseover";
			}
		},
		onClose(event) {
			// Escape key
			if (event.keyCode === 27) {
				this.closeModal();
			}
		},
	},
};
</script>

<style scoped>
.limit-height {
	max-height: calc(100vh - 300px);
}
</style>
