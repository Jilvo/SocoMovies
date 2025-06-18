<template>
  <header class="header">
    <h1>SocoMovies</h1>
    <nav>
      <a href="/">Home</a>
      <a href="/all-movies">All movies</a>
    </nav>
  </header>
</template>

<script setup></script>

<style scoped>
  .header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #222;
    color: #fff;
    padding: 1rem 2rem;
  }

  nav a {
    color: #fff;
    margin-left: 1.5rem;
    text-decoration: none;
    font-weight: 500;
  }

  nav a:hover {
    text-decoration: underline;
  }
</style>
