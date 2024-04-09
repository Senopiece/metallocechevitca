<script>
  import { createEventDispatcher } from "svelte";
  let text = "";
  let imageFile = null;
  let imagePreviewUrl = null;
  const dispatch = createEventDispatcher();
  let inputMode = "text"; // Possible values: 'text', 'image'
  let isDraggingOver = false; // Tracks drag state

  function switchInputMode() {
    if (inputMode === "text") {
      inputMode = "image";
      text = ""; // Optionally clear text when switching to image input
    } else {
      inputMode = "text";
      imageFile = null;
      imagePreviewUrl = null; // Optionally clear image when switching back to text input
    }
  }

  function processFile(file) {
    if (file && file.type.startsWith("image/")) {
      imageFile = file;
      imagePreviewUrl = URL.createObjectURL(file);
      dispatch("imageSelected", { file });
    }
  }

  function handleImageChange(event) {
    const file = event.target.files[0];
    processFile(file);
  }

  function handleDragOver(event) {
    event.preventDefault();
  }

  function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    processFile(file);
    isDraggingOver = false; // Reset drag over state
  }

  function handleDragEnter(event) {
    event.preventDefault();
    isDraggingOver = true;
  }

  function handleDragLeave(event) {
    event.preventDefault();
    isDraggingOver = false;
  }
</script>

<div>
  {#if inputMode === "text"}
    <input type="text" placeholder="Enter some text" bind:value={text} />
  {:else}
    <input
      type="file"
      accept="image/*"
      capture="environment"
      id="fileInput"
      on:change={handleImageChange}
      hidden
    />
    <label
      for="fileInput"
      class="drop-zone"
      on:dragover={handleDragOver}
      on:drop={handleDrop}
      on:dragenter={handleDragEnter}
      on:dragleave={handleDragLeave}
      class:drag-over={isDraggingOver}
    >
      Drag and drop an image here, or click to select
    </label>
    {#if imagePreviewUrl}
      <img class="preview-img" src={imagePreviewUrl} alt="Image preview" />
    {/if}
  {/if}
  <button class="switch-button" on:click={switchInputMode}>
    Switch to {inputMode === "text" ? "Image" : "Text"} Input
  </button>
</div>

<style>
  .drop-zone {
    border: 2px dashed #ccc;
    border-radius: 5px;
    padding: 20px;
    text-align: center;
    margin-top: 10px;
    color: #ccc;
  }

  .drop-zone.drag-over {
    border-color: #000;
    color: #000;
  }

  .preview-img {
    width: 100%; /* Adjust based on your needs */
    height: auto;
    display: block;
    margin-top: 10px;
  }

  .switch-button {
    display: block;
    margin: 20px 0;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
</style>
