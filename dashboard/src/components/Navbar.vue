<template>
	<nav class="bg-white px-8 pt-4 shadow-sm">
		<div class="container mx-auto">
			<Logo />
			<div class="flex mt-3 justify-between">
				<div class="-mb-px flex items-end">
					<a
						class="no-underline text-teal-500 border-b-2 border-teal-500 uppercase tracking-wider font-bold text-xs py-3 mr-8"
						href="#"
					>
						All Bookmarks
					</a>
					<a
						class="no-underline text-gray-600 border-b-2 border-transparent uppercase tracking-wider font-bold text-xs py-3 mr-8"
						href="#"
					>
						Tags
					</a>
					<a
						class="no-underline text-gray-600 border-b-2 border-transparent uppercase tracking-wider font-bold text-xs py-3"
						href="#"
					>
						Archive
					</a>
				</div>
				<div class="flex">
					<Search class="mb-3 mr-2" />
					<NavbarNew class="pt-2" />
				</div>
			</div>
		</div>
	</nav>
</template>

<script>
import Logo from "@/components/Logo.vue";
import Search from "@/components/Search.vue";
import NavbarNew from "@/components/NavbarNew.vue";

export default {
	name: "Navbar",
	components: {
		Logo,
		Search,
		NavbarNew,
	},
};
</script>

<style></style>
