<script>
  import TextImageInput from "./components/TextImageInput.svelte";
  import LimitNumberInput from "./components/LimitNumberInput.svelte";
  import MultiChoiceDropdown from "./components/MultiChoiceDropdown.svelte";

  function handleUpdate(event) {
    console.log(event.detail);
  }

  let options = [
    { id: 1, name: "Option 1", selected: false },
    { id: 2, name: "Option 2", selected: false },
    { id: 3, name: "Option 3", selected: false },
  ];
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
