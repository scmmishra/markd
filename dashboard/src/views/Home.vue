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
	methods: {
		fetch: async function() {
			this.fetchedData = await this.$call("get_bookmarks");
		},
	},
	async mounted() {
		this.fetch();
	},
	created() {
		this.$eventHub.$on("updated-links", this.fetch);
	},
	beforeDestroy() {
		this.$eventHub.$off("updated-links");
	},
};
</script>
