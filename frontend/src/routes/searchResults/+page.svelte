<script lang="ts">
	import 'leaflet/dist/leaflet.css';
	import 'leaflet-routing-machine/dist/leaflet-routing-machine.css';
	import { onMount } from 'svelte';
	import L from 'leaflet';
	import 'leaflet-routing-machine'; // Make sure leaflet-routing-machine is imported
	import { searchResultsStore } from '$lib/services/SearchResultStore';
	import type { SearchResultsStore } from '$lib/structs/SerachResult';
	import { goto } from '$app/navigation';

	let mapContainer; // DOM element to bind the map
	let searchResults: SearchResultsStore | null;

	let imageUrl: string;

	searchResultsStore.subscribe(($searchResults) => {
		searchResults = $searchResults;

		if (searchResults?.type === 'image') {
			imageUrl = URL.createObjectURL(searchResults.image);
		}
	});

	onMount(() => {
		if (searchResults?.res?.places && searchResults.res.places.length > 0) {
			const initialPlace = searchResults.res.places[0];
			const map = L.map(mapContainer).setView([initialPlace.Lat, initialPlace.Lon], 13);

			L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
				attribution:
					'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
			}).addTo(map);

			let optimal_route = searchResults.res.optimal_route;
			if (optimal_route !== null) {
				const waypoints = optimal_route.map((ll) => L.latLng(ll.Lat, ll.Lon));
				L.Routing.control({
					waypoints: waypoints,
					routeWhileDragging: true,
					addWaypoints: false,
					createMarker: function () {
						return null;
					} // Prevent automatic marker creation
				}).addTo(map);
			}

			// Add markers and tooltips for each place
			searchResults.res.places.forEach((place) => {
				const marker = L.marker([place.Lat, place.Lon]).addTo(map);
				marker
					.bindTooltip(place.Name + ' : ' + place.probability, {
						permanent: false,
						direction: 'right'
					})
					.closeTooltip();
				marker.on('click', () => {
					goto(`/place/${place.XID}`);
				});
			});
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
		<div bind:this={mapContainer} class="map"></div>
	{:else}
		<p>No search results to display.</p>
	{/if}
</main>

<style>
	.map {
		height: 400px;
		width: 100%;
	}
</style>
