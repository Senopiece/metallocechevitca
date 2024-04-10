<script lang="ts">
	import { getPlacesImpl, getPlacesApiPath } from '$lib/services/Places';
	import { type PlaceInfo } from '$lib/structs/Places.js';
	import { onMount } from 'svelte';

	const api = getPlacesApiPath();
	const placesapi = getPlacesImpl();

	export let data;
	let xid: string;

	$: xid = data.slug;

	let placeInfo: PlaceInfo | undefined;

	onMount(async () => {
		placeInfo = await placesapi.getPlaceInfo(xid);
	});
</script>

{#if placeInfo}
	<div>
		<h2>Category: {placeInfo.category}</h2>
		{#if placeInfo.images.length > 0}
			<div class="images">
				{#each placeInfo.images as imageId}
					<img src={`${api}/image/${imageId}`} alt="Image {imageId}" />
				{/each}
			</div>
		{:else}
			<p>No images available.</p>
		{/if}
	</div>
{:else}
	<p>Loading place info...</p>
{/if}

<style>
	.images img {
		width: 100%; /* Adjust based on your layout needs */
		margin-bottom: 1rem;
	}
</style>
