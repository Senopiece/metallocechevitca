<script lang="ts">
	import { createEventDispatcher, onMount } from 'svelte';

	const dispatch = createEventDispatcher<{ update: number }>();

	export let maxLimit = 10;
	let value = maxLimit;

	function updateValue(event: any) {
		// Use a type assertion to tell TypeScript the target is an input element
		let inputElement = event.target as HTMLInputElement;
		let inputValue = +inputElement.value;

		if (inputValue > maxLimit) {
			value = maxLimit;
		} else if (inputValue < 0) {
			value = 0;
		} else {
			value = inputValue;
		}

		// Dispatch the update event with the new value
		dispatch('update', value);
	}

	onMount(() => {
		dispatch('update', value);
	});
</script>

<div>
	<span>Limit: </span>
	<input type="number" bind:value on:input={updateValue} />
</div>
