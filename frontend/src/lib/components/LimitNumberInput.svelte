<script lang="ts">
	import { createEventDispatcher, onMount } from 'svelte';

	const dispatch = createEventDispatcher<{ update: number }>();

	export let maxLimit = 10;
	let value = maxLimit;

	function updateValue(event: any) {
		let inputElement = event.target as HTMLInputElement;
		let inputValue = +inputElement.value;

		if (inputValue > maxLimit) {
			value = maxLimit;
		} else if (inputValue < 0) {
			value = 0;
		} else {
			value = inputValue;
		}

		dispatch('update', value);
	}

	onMount(() => {
		dispatch('update', value);
	});
</script>

<div class="input-container">
	<span>Лимит: </span>
	<input type="number" bind:value on:input={updateValue} />
</div>

<style>
	.input-container {
		display: flex;
		align-items: center;
		font-family: sans-serif;
		color: #333;
	}

	.input-container > span {
		margin-right: 8px;
	}

	input[type='number'] {
		outline: none;
		border: none;
		background-color: transparent;
		padding: 8px 0;
		font-size: 16px;
		width: 40px;
		color: inherit;
		-webkit-appearance: textfield;
		overflow: hidden; /* Might want to hide overflow if the value is wider than the input */
	}

	input[type='number']::-webkit-inner-spin-button,
	input[type='number']::-webkit-outer-spin-button,
	input[type='number']::-moz-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}

	input[type='number']:focus {
		border: none;
		box-shadow: none;
	}
</style>
