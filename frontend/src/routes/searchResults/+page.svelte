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
		<h1>Результаты поиска</h1>
		{#if searchResults?.type === 'image'}
			<img src={imageUrl} alt="Search image" />
		{/if}
		{#if searchResults.type === 'text'}
			{#each searchResults.res.places as place}
				<div>
					<h2><a href="/place/{place.XID}">{place.Name} : {place.probability}</a></h2>
				</div>
			{/each}
		{:else}
			<!-- Assuming it's an image search result -->
			{#each searchResults.res.places as place}
				<div>
					<h2><a href="/place/{place.XID}">{place.Name} : {place.probability}</a></h2>
				</div>
			{/each}
			<!-- Optionally display the image or categories -->
		{/if}
	{:else}
		<p>No search results to display.</p>
	{/if}
</main>
