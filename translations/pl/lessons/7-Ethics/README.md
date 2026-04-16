# Etyka i Odpowiedzialna Sztuczna Inteligencja

Jesteś już prawie na końcu tego kursu i mam nadzieję, że teraz wyraźnie widzisz, że sztuczna inteligencja opiera się na szeregu formalnych metod matematycznych, które pozwalają nam znajdować zależności w danych i trenować modele, aby odtwarzały pewne aspekty ludzkiego zachowania. W obecnym momencie historii uważamy AI za bardzo potężne narzędzie do wydobywania wzorców z danych i stosowania tych wzorców do rozwiązywania nowych problemów.

## [Quiz przed wykładem](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Jednak w literaturze science fiction często spotykamy się z historiami, w których AI stanowi zagrożenie dla ludzkości. Zazwyczaj te historie koncentrują się wokół jakiegoś rodzaju buntu AI, kiedy to AI decyduje się przeciwstawić ludziom. To sugeruje, że AI posiada pewne emocje lub może podejmować decyzje nieprzewidziane przez swoich twórców.

Rodzaj AI, o którym uczyliśmy się w tym kursie, to nic innego jak duże obliczenia macierzowe. Jest to bardzo potężne narzędzie, które pomaga nam rozwiązywać nasze problemy, i jak każde inne potężne narzędzie - może być używane zarówno w dobrych, jak i złych celach. Co ważne, może być również *niewłaściwie używane*.

## Zasady Odpowiedzialnej Sztucznej Inteligencji

Aby uniknąć przypadkowego lub celowego niewłaściwego użycia AI, Microsoft określa ważne [Zasady Odpowiedzialnej Sztucznej Inteligencji](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Poniższe koncepcje stanowią podstawę tych zasad:

* **Sprawiedliwość** odnosi się do ważnego problemu *uprzedzeń modelu*, które mogą wynikać z użycia stronniczych danych do treningu. Na przykład, gdy próbujemy przewidzieć prawdopodobieństwo zdobycia pracy jako programista przez daną osobę, model może preferować mężczyzn - tylko dlatego, że zestaw danych treningowych prawdopodobnie był stronniczy w kierunku męskiej grupy odbiorców. Musimy starannie zrównoważyć dane treningowe i badać model, aby unikać uprzedzeń i upewnić się, że model uwzględnia bardziej istotne cechy.
* **Niezawodność i Bezpieczeństwo**. Z natury rzeczy modele AI mogą popełniać błędy. Sieć neuronowa zwraca prawdopodobieństwa, co musimy brać pod uwagę przy podejmowaniu decyzji. Każdy model ma pewną precyzję i czułość, i musimy to rozumieć, aby zapobiec szkodom, jakie mogą wyrządzić błędne porady.
* **Prywatność i Bezpieczeństwo** mają pewne specyficzne implikacje dla AI. Na przykład, gdy używamy danych do trenowania modelu, te dane w pewnym sensie stają się "zintegrowane" z modelem. Z jednej strony zwiększa to bezpieczeństwo i prywatność, z drugiej - musimy pamiętać, na jakich danych model był trenowany.
* **Inkluzywność** oznacza, że nie budujemy AI, aby zastąpić ludzi, ale raczej aby wspierać ludzi i uczynić naszą pracę bardziej kreatywną. Jest to również związane ze sprawiedliwością, ponieważ w przypadku społeczności niedostatecznie reprezentowanych większość zbieranych przez nas zestawów danych prawdopodobnie będzie stronnicza, i musimy upewnić się, że te społeczności są uwzględnione i odpowiednio obsługiwane przez AI.
* **Przejrzystość**. Obejmuje to upewnienie się, że zawsze jasno informujemy o użyciu AI. Ponadto, tam gdzie to możliwe, chcemy używać systemów AI, które są *interpretowalne*.
* **Odpowiedzialność**. Gdy modele AI podejmują pewne decyzje, nie zawsze jest jasne, kto jest za nie odpowiedzialny. Musimy upewnić się, że rozumiemy, gdzie leży odpowiedzialność za decyzje AI. W większości przypadków chcielibyśmy włączyć ludzi w proces podejmowania ważnych decyzji, aby to faktyczni ludzie byli odpowiedzialni.

## Narzędzia do Odpowiedzialnej Sztucznej Inteligencji

Microsoft opracował [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), który zawiera zestaw narzędzi:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard, który obejmuje:

   - EconML - narzędzie do analizy przyczynowej, koncentrujące się na pytaniach typu "co by było, gdyby"
   - DiCE - narzędzie do analizy kontrfaktycznej, pozwalające zobaczyć, które cechy należy zmienić, aby wpłynąć na decyzję modelu

Więcej informacji na temat etyki AI znajdziesz w [tej lekcji](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) w programie nauczania Machine Learning, która zawiera również zadania.

## Przegląd i Samodzielna Nauka

Weź udział w [ścieżce nauki](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste), aby dowiedzieć się więcej o odpowiedzialnej sztucznej inteligencji.

## [Quiz po wykładzie](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.