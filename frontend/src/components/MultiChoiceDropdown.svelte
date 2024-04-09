<script>
  export let options = [];
  let isDropdownOpen = false;

  function toggleSelectAll() {
    const newSelectionValue = !allSelected;
    options = options.map((option) => ({
      ...option,
      selected: newSelectionValue,
    }));
  }

  $: allSelected = options.every((option) => option.selected);
</script>

<div class="dropdown">
  <button on:click={() => (isDropdownOpen = !isDropdownOpen)}>
    Select Options
  </button>
  {#if isDropdownOpen}
    <div class="dropdown-menu">
      <label>
        <input
          type="checkbox"
          checked={allSelected}
          on:change={toggleSelectAll}
        />
        Select All
      </label>
      {#each options as option}
        <label>
          <input type="checkbox" bind:checked={option.selected} />
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
