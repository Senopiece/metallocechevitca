<script lang="ts">
	import { createEventDispatcher, onMount, onDestroy } from 'svelte';

	export let options: DropdownElem[] = [];
	let isDropdownOpen = false;
	let dropdownElement;

	const dispatch = createEventDispatcher<{
		selected: number[];
	}>();

	function toggleSelectAll() {
		const newSelectionValue = !allSelected;
		options = options.map((option) => ({
			...option,
			selected: newSelectionValue
		}));
		dispatchSelectedOptions();
	}

	function dispatchSelectedOptions() {
		dispatch('selected', selectedIds);
	}

	onMount(() => {
		dispatch('selected', selectedIds);

		const handleClickOutside = (event) => {
			if (!dropdownElement.contains(event.target)) {
				isDropdownOpen = false;
			}
		};

		window.addEventListener('click', handleClickOutside);

		// Cleanup event listener on component destruction
		onDestroy(() => {
			window.removeEventListener('click', handleClickOutside);
		});
	});

	function handleDropdownClick(event) {
		// Prevent click inside dropdown from reaching window
		event.stopPropagation();
	}

	$: selectedIds = options.filter((option) => option.selected).map((option) => option.id);
	$: options, dispatchSelectedOptions();
	$: allSelected = options.every((option) => option.selected && options.length > 0);
</script>

<div class="dropdown" bind:this={dropdownElement} on:click={handleDropdownClick}>
	<button on:click={() => (isDropdownOpen = !isDropdownOpen)}> Выбрать города </button>
	{#if isDropdownOpen}
		<div class="dropdown-menu">
			<label>
				<input type="checkbox" checked={allSelected} on:change={toggleSelectAll} />
				Выбрать все
			</label>
			{#each options as option}
				<label>
					<input
						type="checkbox"
						bind:checked={option.selected}
						on:change={dispatchSelectedOptions}
					/>
					{option.name}
				</label>
			{/each}
		</div>
	{/if}
</div>

<style>
	.dropdown-menu {
		border: 1px solid #ccc;
		padding: 10px;
		margin-top: 5px;
		background: white;
		position: absolute;
	}
	label {
		display: block;
		cursor: pointer;
	}
	button {
		cursor: pointer;
	}
</style>
