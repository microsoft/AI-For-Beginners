<template>
  <div>
    <nav>
      <ul>
        <li>
          <router-link class="navlink" to="/">Home</router-link>
        </li>
        <li>
          <label for="locale">locale</label>
        </li>
        <li>
          <select v-model="locale">
            <option>en</option>
            <option>es</option>
          </select>
        </li>
        <li class="title">{{ questions[locale][0].title }}</li>
      </ul>
    </nav>
    <div id="app">
      
      <router-view>
        <Quiz />
      </router-view>
    </div>
  </div>
</template>

<script>
import Quiz from "@/components/Quiz.vue";
import messages from "@/assets/translations";

export default {
  name: "App",
  computed: {
    questions() {
      return messages;
    },
    
  },
  i18n: { messages },
  components: {
    Quiz,
  },
  data() {
    return {
      locale: "",
    };
  },
  watch: {
    locale(val) {
      this.$root.$i18n.locale = val;
    },
  },
  created() {
    this.route = this.$route.params.id;
    if (this.$route.query.loc) {
      this.locale = this.$route.query.loc;
    } else {
      this.locale = "en";
    }
  },
};
</script>

<style>
html {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #252d4a;
}
nav {
  background-color: #252d4a;
  padding: 1em;
  margin-bottom: 20px;
}

nav a {
  color: white;
  text-align: right;
}

ul{
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

li {
  float: left;
}

.title {
  color:white;
  font-weight: bold;
  font-size: x-large;
  float: right;
}

.link {
  display: list-item;
}

h1,
h2,
h3,
.message {
  text-align: center;
}
.error {
  color: red;
}
.complete {
  color: green;
}
.card {
  width: 60%;
  border: #252d4a solid;
  border-radius: 5px;
  margin: auto;
  padding: 1em;
}
.btn {
  min-width: 50%;
  font-size: 16px;
  text-align: center;
  cursor: pointer;
  margin-bottom: 5px;
  width: 50%;
  font-size: 16px;
  color: #ffffff;
  background-color: #252d4a;
  border-radius: 5px;
  padding: 5px;
  justify-content: flex-start;
  align-items: center;
}
.ans-btn {
  justify-content: center;
  display: flex;
  margin: 4px auto;
}
</style>
