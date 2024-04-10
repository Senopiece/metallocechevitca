<script lang="ts">
	import { searchResultsStore } from '$lib/services/SearchResultStore';
	import type { SearchResultsStore } from '$lib/structs/SerachResult';

	let imageUrl: string;

	// Subscribe to the store
	let searchResults: SearchResultsStore | null;
	searchResultsStore.subscribe(($searchResults) => {
		searchResults = $searchResults;

		if (searchResults?.type === 'image') {
			imageUrl = URL.createObjectURL(searchResults.image);
		}
	});
</script>

<main>
	{#if searchResults}
		<h1>Загруженное изображение</h1>
		{#if searchResults?.type === 'image'}
			<img src={imageUrl} alt="Search image" />
			{#each searchResults.res.categories as category}
				<div>
					<h2>{category.category} : {category.probability}</h2>
				</div>
			{/each}
		{/if}
		<h1>Результаты поиска</h1>
		{#each searchResults.res.places as place}
			<div>
				<h2><a href="/place/{place.XID}">{place.Name} : {place.probability}</a></h2>
			</div>
		{/each}
	{:else}
		<p>No search results to display.</p>
	{/if}
</main>
