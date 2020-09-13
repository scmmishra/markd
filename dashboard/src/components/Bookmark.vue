<template>
	<div class="bg-white shadow hover:shadow-md rounded-lg p-2 cursor-pointer">
		<div @click="openPreview" class="h-full">
			<img
				:src="mark.image"
				class="rounded-md h-40 text-center object-cover"
			/>
			<div class="flex flex-col justify-between">
				<h3 class="text-lg font-bold mt-2">
					{{ mark.meta_title | truncate(50) }}
				</h3>
				<p class="text-gray-600 text-sm">
					{{ mark.website }}
				</p>
			</div>
		</div>
		<ArticlePreview v-if="showPreview" @close="closePreview" :mark="mark" />
	</div>
</template>
<script>
import ArticlePreview from "@/components/ArticlePreview";

export default {
	name: "Bookmark",
	props: ["mark"],
	components: {
		ArticlePreview,
	},
	data() {
		return {
			showPreview: false,
		};
	},
	methods: {
		openPreview: function() {
			this.showPreview = true;
		},
		closePreview: function() {
			this.showPreview = false;
		},
	},
};
</script>
