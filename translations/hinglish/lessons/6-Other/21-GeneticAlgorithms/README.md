# Genetic Algorithms

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetic Algorithms** (GA) ek **evolutionary approach** par based hain, jisme kisi problem ka optimal solution paane ke liye population ke evolution ke methods use kiye jate hain. Inhe 1975 mein [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) ne propose kiya tha.

Genetic Algorithms in ideas par based hain:

* Problem ke valid solutions ko **genes** ke roop mein represent kiya ja sakta hai.
* **Crossover** hamein do solutions ko combine karke ek naya valid solution paane deta hai.
* **Selection** ka use kisi **fitness function** ke through zyada optimal solutions chunne ke liye hota hai.
* **Mutations** isliye introduce kiye jate hain ki optimization ko destabilize kiya ja sake aur hamein local minimum se bahar nikala ja sake.

Agar aap Genetic Algorithm implement karna chahte hain, toh aapko in cheezon ki zaroorat hogi:

 * Apne problem solutions ko **genes** g&in;&Gamma; use karke code karne ka tareeka dhoondhiye.
 * Genes ke set &Gamma; par **fitness function** fit: &Gamma;&rightarrow;**R** define kijiye. Chhote function values behtar solution ko dikhate hain.
 * Do genes ko combine karke ek naya valid solution paane ke liye **crossover** mechanism define kijiye crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * **Mutation** mechanism define kijiye mutate: &Gamma;&rightarrow;&Gamma;.

Kai cases mein, crossover aur mutation genes ko numerical sequences ya bit vectors ki tarah manipulate karne ke liye kaafi simple algorithms hote hain.

Genetic Algorithm ka specific implementation case-to-case alag ho sakta hai, lekin overall structure yeh hai:

1. Ek initial population G&subset;&Gamma; chuniye.
2. Is step mein perform kiya jane wala operation randomly chuniye: crossover ya mutation.
3. **Crossover**:
  * Do genes g<sub>1</sub>, g<sub>2</sub> &in; G randomly chuniye.
  * Crossover calculate kijiye g=crossover(g<sub>1</sub>,g<sub>2</sub>).
  * Agar fit(g)<fit(g<sub>1</sub>) ya fit(g)<fit(g<sub>2</sub>) - toh population mein corresponding gene ko g se replace kijiye.
4. **Mutation** - random gene g&in;G chuniye aur use mutate(g) se replace kijiye.
5. Step 2 se repeat kijiye, jab tak fit ki value kaafi chhoti na ho jaye, ya steps ki limit tak na pahunch jayein.

## Typical Tasks

Genetic Algorithms se aam taur par solve kiye jane wale tasks mein yeh shamil hain:

1. Schedule optimization
1. Optimal packing
1. Optimal cutting
1. Exhaustive search ko speed up karna

## ✍️ Exercise: Genetic Algorithms

Apni learning agle notebooks mein jaari rakhiye:

[Is notebook](Genetic.ipynb) par jaiye aur Genetic Algorithms use karne ke do examples dekhiye:

1. Treasure ka fair division
1. 8 Queens Problem

## Conclusion

Genetic Algorithms ka use kai problems solve karne ke liye hota hai, jisme logistics aur search problems shamil hain. Yeh field psychology aur computer science ke topics ko mix karne wali research se inspired hai.

## 🚀 Challenge

"Genetic algorithms implement karna aasaan hai, lekin unke behavior ko samajhna mushkil hai." [Source](https://wikipedia.org/wiki/Genetic_algorithm) Research kijiye aur Genetic Algorithm ka koi implementation dhoondhiye, jaise Sudoku puzzle solve karna, aur use sketch ya flowchart ke roop mein explain kijiye.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Review & Self Study

[Yeh shandaar video](https://www.youtube.com/watch?v=qv6UVOQ0F44) dekhiye, jisme bataya gaya hai ki computer Genetic Algorithms se train kiye gaye neural network ka use karke Super Mario khelna kaise seekh sakta hai. Is tarah ke games khelna computer ko kaise sikhaya jata hai, iske baare mein hum [agle section](../22-DeepRL/README.md) mein aur seekhenge.

## [Assignment: Diophantine Equations](Diophantine.ipynb)

Aapka goal so-called **Diophantine equation** ko solve karna hai - ek equation jiske integer roots hote hain. Jaise ki, equation a+2b+3c+4d=30 par vichar kijiye. Aapko woh integer roots dhoondhne hain jo is equation ko satisfy karte hain.

*Yeh assignment [is post](https://habr.com/post/128704/) se inspired hai.*

Hints:

1. Aap roots ko [0;30] interval mein maan sakte hain.
1. Gene ke roop mein, roots ki values ki list use karne ke baare mein sochiye.

[Diophantine.ipynb](Diophantine.ipynb) ko starting point ke roop mein use kijiye.

---

