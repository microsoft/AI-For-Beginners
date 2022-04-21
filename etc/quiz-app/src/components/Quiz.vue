<template>
  <div class="card">
    <div v-for="q in questions[currLocale]" :key="q.quizzes[0].id">
      <div v-for="quiz in q.quizzes" :key="quiz.id">
        
        <div v-if="route == quiz.id">
          <div>
            <h3 v-if="complete" class="message complete">{{ q.complete }}</h3>
            <div v-else>
              <h3 v-if="error" class="error">{{ q.error }}</h3>
            </div>

            <h1>{{quiz.title}}</h1>


            <h2>
              {{ quiz.quiz[currentQuestion].questionText }}
            </h2>
            <div>
              <button
                :key="index"
                v-for="(option, index) in quiz.quiz[currentQuestion]
                  .answerOptions"
                @click="handleAnswerClick(option.isCorrect)"
                class="btn ans-btn"
              >
                {{ option.answerText }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import messages from "@/assets/translations";

export default {
  name: "Quiz",
  data() {
    return {
      currentQuestion: 0,
      complete: false,
      error: false,
      route: "",
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

  i18n: {
    messages,
  },

  methods: {
    handleAnswerClick(isCorrect) {
      this.error = false;
      let nextQuestion = this.currentQuestion + 1;
      if (isCorrect == "true") {
        //always 3 questions per quiz
        if (nextQuestion < 3) {
          this.currentQuestion = nextQuestion;
        } else {
          this.complete = true;
        }
      } else {
        this.error = true;
      }
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
