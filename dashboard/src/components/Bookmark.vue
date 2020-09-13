<template>
	<div
		class="bg-white shadow hover:shadow-md rounded-lg p-2"
		@click="$refs.previewModal.openModal()"
	>
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
		<ArticlePreview ref="previewModal" :mark="mark" />
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
};
</script>
