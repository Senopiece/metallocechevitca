<script>
  import TextImageInput from "./components/TextImageInput.svelte";
  import LimitNumberInput from "./components/LimitNumberInput.svelte";

  function handleUpdate(event) {
    console.log(event.detail);
  }
</script>

<main>
  <TextImageInput />
  <LimitNumberInput on:update={handleUpdate} />
</main>

<style>
  main {
    padding: 1rem;
    font-family: Arial, sans-serif;
  }
</style>
