<script lang="ts">
  import TextImageInput from "$lib/components/TextImageInput.svelte";
  import LimitNumberInput from "$lib/components/LimitNumberInput.svelte";
  import MultiChoiceDropdown from "$lib/components/MultiChoiceDropdown.svelte";

  function handleUpdate(event: any) {
    console.log(event.detail);
  }

  export let options: DropdownElem[] = [];
</script>

<main>
  <TextImageInput />
  <MultiChoiceDropdown {options} />
  <LimitNumberInput on:update={handleUpdate} />
</main>

<style>
  main {
    padding: 1rem;
    font-family: Arial, sans-serif;
  }
</style>
  