<template>
	<div>
		<button
			class="bg-teal-500 text-white active:bg-teal-600 font-bold uppercase text-sm px-6 py-2 rounded shadow hover:shadow-lg outline-none focus:outline-none"
			type="button"
			style="transition: all .15s ease"
			v-on:click="toggleModal()"
		>
			MARK
		</button>
		<div
			v-if="showModal"
			class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex"
		>
			<div class="relative w-1/3 my-6 mx-auto max-w-md">
				<!--content-->
				<div
					class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none"
				>
					<!--header-->
					<div
						class="flex items-start justify-between px-5 py-3 border-gray-300 rounded-t"
					>
						<h3 class="text-xl font-semibold">
							Add Mark
						</h3>
						<button
							class="flex items-center ml-auto bg-transparent border-0 text-black float-right text-3xl leading-none font-semibold outline-none focus:outline-none"
							v-on:click="toggleModal()"
						>
							<span
								class="bg-transparent text-gray-400 opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none"
							>
								×
							</span>
						</button>
					</div>
					<!--body-->
					<div class="relative px-5 py-3 flex-auto">
						<input
							type="text"
							v-model="url"
							:disabled="freeze"
							placeholder="https://getmarkd.app"
							class="px-3 py-3
						placeholder-gray-400 text-gray-700 relative bg-gray-200
						rounded text-sm outline-none focus:outline-none w-full"
						/>
					</div>
					<!--footer-->
					<div class="flex items-center justify-end p-2 rounded-b">
						<button
							class="text-white bg-teal-500 rounded font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1"
							type="button"
							:disabled="freeze"
							style="transition: all .15s ease"
							v-on:click="saveURL()"
						>
							mark it.
						</button>
					</div>
				</div>
			</div>
		</div>
		<div
			v-if="showModal"
			class="opacity-25 fixed inset-0 z-40 bg-black"
		></div>
	</div>
</template>

<script>
export default {
	name: "NavbarNew",
	data() {
		return {
			showModal: false,
			freeze: false,
			url: "",
		};
	},
	methods: {
		toggleModal: function() {
			this.showModal = !this.showModal;
		},
		saveURL: function() {
			this.freeze = true;
			this.$call("save_mark", {
				url: this.url,
			}).then((data) => {
				if (data) {
					this.freeze = false;
					this.showModal = false;
					this.$eventHub.$emit("updated-links");
				}
			});
		},
	},
};
</script>

<style></style>
