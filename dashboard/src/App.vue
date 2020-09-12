<template>
	<div id="app" class="">
		<Navbar />
		<router-view class="container mx-auto" />
	</div>
</template>

<script>
// @ is an alias to /src
import Navbar from "@/components/Navbar.vue";

export default {
	name: "App",
	components: {
		Navbar,
	},
};
</script>
