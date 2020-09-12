<template>
	<transition name="fade">
		<div class="fixed z-10 inset-0 overflow-y-auto" v-if="show">
			<div
				class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
			>
				<div class="fixed inset-0 transition-opacity">
					<div class="absolute inset-0 bg-gray-500 opacity-75"></div>
				</div>

				<span
					class="hidden sm:inline-block sm:align-middle sm:h-screen"
				></span>
				<div
					class="w-2/3 inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8"
					role="dialog"
					aria-modal="true"
					aria-labelledby="modal-headline"
				>
					<div
						class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4 w-2/3 mx-auto my-12"
					>
						<div class="prose prose-md">
							<h2
								class="text-2xl leading-6 font-medium text-gray-900"
								id="modal-headline"
							>
								<slot name="header" />
							</h2>
							<div class="mt-2 overflow-scroll limit-height">
								<slot name="body" />
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</transition>
</template>

<script>
export default {
	name: "ArticlePreview",
	data() {
		return {
			show: false,
		};
	},
	methods: {
		closeModal() {
			this.show = false;
			document.querySelector("body").classList.remove("overflow-hidden");
		},
		openModal() {
			this.show = true;
			document.querySelector("body").classList.add("overflow-hidden");
		},
	},
};
</script>

<style scoped>
.limit-height {
	max-height: calc(100vh - 300px);
}
</style>
