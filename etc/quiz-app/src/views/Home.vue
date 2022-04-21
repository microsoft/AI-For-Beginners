<template>
<div>
  <div v-for="q in questions[currLocale]" :key="q.id">
     
      <router-link
        v-for="quiz in q.quizzes"
        :key="quiz.id"
        :to="`quiz/${quiz.id}`"
        class="link"
      >
        {{ quiz.title }}
      </router-link>
   
  </div>
  </div>
</template>

<script>
import messages from "@/assets/translations";

export default {
  name: "Home",
  data() {
    return {
      locale: "",
    };
  },
  computed: {
    questions() {
      return messages;
    },
    currLocale() {
      return this.$root.$i18n.locale;
    }
  },
  i18n: { messages },
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