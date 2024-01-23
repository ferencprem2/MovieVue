<script>
import {ref} from 'vue'
export default { 
  data() {
    return {
      movies: [],
      numberOfFullStars: ref(0),
      numberOfBlankStars: ref(0),
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/movies/')
        if (!response.ok){
          throw new Error('Response was not ok')
        }
        const data = await response.json()
        console.log(data)
        this.movies = data
      } catch (error) {
        console.error('Fetch error: ', error)
      }
    },
    replaceStaticWithAssets(url) {
      return url.replace('static', 'assets')
    },
    displayStarByRating(rating) {
      var fullStar = "&#9733" 
      return fullStar
      
    }
  }
}

</script>
<!-- &#9733 9734 -->
<template>
<div id="movieContainer">
  <div id="movie" v-for="movie in movies">
    <h4><span v-for="index in numberOfFullStars" :key="index">&#9733</span></h4>
    <img :src="replaceStaticWithAssets(movie.poster_image)" alt="">
    <h4>{{movie.title}}</h4>
  </div>
</div>
</template>

<style>
body{
  background: linear-gradient( orange, purple );
}


#movieContainer{
  background-color: black;
  color: white;
  display: flex;
  flex-direction: row;
}
#movie{
  border: 1px solid black;
}

#movie>img{
  height: 300px;
  width: 150px;
}
</style>
