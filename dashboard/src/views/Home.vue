<template>
	<div>
		<div class="grid grid-cols-4 gap-4 mt-5">
			<Bookmark
				v-for="mark in fetchedData"
				:mark="mark"
				:key="mark.name"
			/>
		</div>
	</div>
</template>

<script>
// @ is an alias to /src
import Bookmark from "@/components/Bookmark";

export default {
	name: "Home",
	components: {
		Bookmark,
	},
	data() {
		return {
			fetchedData: [],
		};
	},
	async mounted() {
		this.fetchedData = await this.$call("get_bookmarks");
	},
};
</script>
