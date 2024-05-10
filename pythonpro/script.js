// script.js

document.addEventListener("DOMContentLoaded", function() {
  // questions verisini al
  var questionsScript = document.getElementById("questions-data");
  var questionsData = JSON.parse(questionsScript.textContent);

  document.getElementById("quiz-form").addEventListener("submit", function(event) {
      event.preventDefault(); // Formun otomatik olarak gönderilmesini engelle

      // Cevapları al
      const formElements = event.target.elements;
      let score = 0;
      for (let i = 0; i < formElements.length; i++) {
          const element = formElements[i];
          if (element.type === "radio" && element.checked) {
              const questionId = element.name.substring(8); // "question" kısmını atla
              const question = questionsData[questionId - 1].question;
              const answer = element.value;
              const correctAnswer = questionsData[questionId - 1].correct_answer;
              if (answer === correctAnswer) {
                  score += 1;
              }
          }
      }

      // Sonucu ekrana yazdır
      const resultDiv = document.getElementById("result");
      resultDiv.innerText = `Your score: ${score}/${questionsData.length}`;
  });
});
