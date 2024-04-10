<script lang="ts">
	import 'leaflet/dist/leaflet.css';
	import { Map, TileLayer, Marker, ToolTip } from 'svelte-map-leaflet';
	import { searchResultsStore } from '$lib/services/SearchResultStore';
	import type { SearchResultsStore } from '$lib/structs/SerachResult';
	import { goto } from '$app/navigation';

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
		{#if searchResults?.type === 'image'}
			<h1>Загруженное изображение</h1>
			<img src={imageUrl} alt="Search image" />
			{#each searchResults.res.categories as category}
				<div>
					<h2>{category.category} : {category.probability}</h2>
				</div>
			{/each}
		{/if}
		<h1>Результаты поиска</h1>
		<div class="map">
			<Map
				options={{
					center: [searchResults.res.places[0].Lat, searchResults.res.places[0].Lon],
					zoom: 10
				}}
			>
				<TileLayer name="BasicMap" url={'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'} />
				{#each searchResults.res.places as place}
					<Marker
						name={place.XID}
						latLng={[place.Lat, place.Lon]}
						events={['click']}
						on:click={() => goto(`/place/${place.XID}`)}
					>
						<ToolTip name={'tooltip' + place.XID}>
							<p>{place.Name} : {place.probability}</p>
						</ToolTip>
					</Marker>
				{/each}
			</Map>
		</div>
	{:else}
		<p>No search results to display.</p>
	{/if}
</main>

<style>
	.map {
		height: 400px;
		width: 100%; /* Adjusted for full width */
	}
</style>
