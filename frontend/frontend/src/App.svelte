<script lang="ts">
  let patentNumber = "";
  let loading = false;
  let results: any = null;

  async function analyzePatent() {
    loading = true;

    const response = await fetch(
      "http://127.0.0.1:8000/patents/analyze",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          patent_number: patentNumber
        })
      }
    );

    results = await response.json();

    loading = false;
  }
</script>

<main class="container">
  <h1>Patent Infringement Search</h1>

  <div class="search-bar">
    <input
      bind:value={patentNumber}
      placeholder="Enter patent number"
    />

    <button on:click={analyzePatent}>
      Analyze
    </button>
  </div>

  {#if loading}
    <p>Analyzing patent...</p>
  {/if}

  {#if results}
    <h2>Patent: {results.patent}</h2>

    {#each results.results as product}
      <div class="card">
        <h3>{product.product_name}</h3>

        {#each product.claim_chart as item}
          <div class="claim">
            <p>
              <strong>Claim Element:</strong>
              {item.claim_element}
            </p>

            <p>
              <strong>Evidence:</strong>
              {item.evidence.quote}
            </p>

            <p>
              <strong>Analysis:</strong>
              {item.analysis}
            </p>

            <p>
              <strong>Confidence:</strong>
              {item.confidence}
            </p>
          </div>
        {/each}
      </div>
    {/each}
  {/if}
</main>

<style>
  .container {
    max-width: 900px;
    margin: 40px auto;
    font-family: Arial;
  }

  .search-bar {
    display: flex;
    gap: 10px;
    margin-bottom: 30px;
  }

  input {
    flex: 1;
    padding: 12px;
  }

  button {
    padding: 12px 20px;
    cursor: pointer;
  }

  .card {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
  }

  .claim {
    border-top: 1px solid #eee;
    padding-top: 10px;
    margin-top: 10px;
  }
</style>