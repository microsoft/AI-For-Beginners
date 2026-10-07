# Ethical aur Responsible AI

Aap is course ko lagbhag poora kar chuke hain, aur mujhe umeed hai ki ab tak aap saaf dekh sakte hain ki AI kai formal mathematical methods par based hai, jo humein data mein relationships dhoondhne aur aise models ko train karne dete hain jo kuch had tak human behavior ko replicate karte hain. Is waqt, hum AI ko ek bahut powerful tool maante hain jo data se patterns nikaalta hai aur un patterns ko nayi problems solve karne ke liye apply karta hai.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Lekin, science fiction mein hum aksar aisi kahaniyan dekhte hain jahan AI insaaniyat ke liye khatra ban jaata hai. Aam taur par yeh kahaniyan kisi na kisi tarah ki AI rebellion ke aas-paas ghoomti hain, jab AI insaanon ke khilaf jaane ka decision leta hai. Iska matlab hota hai ki AI mein koi emotion hai ya woh apne developers ke dwara unexpected decisions le sakta hai.

Is course mein humne jis type ke AI ke baare mein seekha hai, woh bas bade matrix arithmetic hai. Yeh humari problems solve karne mein madad karne wala ek bahut powerful tool hai, aur kisi bhi doosre powerful tool ki tarah - ise achhe aur bure dono maqsadon ke liye use kiya ja sakta hai. Sabse important baat yeh hai ki ise *misuse* kiya ja sakta hai.

## Responsible AI ke Principles

AI ke is accidental ya jaanbujh kar kiye gaye misuse se bachne ke liye, Microsoft ne [Responsible AI ke Principles](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) ko important bataya hai. In principles ke peeche yeh concepts hain:

* **Fairness** *model biases* ki important problem se related hai, jo training ke liye biased data use karne se ho sakti hai. Jaise, jab hum kisi person ke software developer ki job paane ki probability predict karne ki koshish karte hain, toh model ke purushon (men) ko zyada preference dene ki sambhavna hoti hai - sirf isliye ki training dataset shayad male audience ki taraf biased tha. Humein training data ko dhyaan se balance karna chahiye aur model ko investigate karna chahiye taaki biases se bacha ja sake, aur yeh sunishchit karna chahiye ki model zyada relevant features ko dhyaan mein rakhe.
* **Reliability aur Safety**. Apni nature ki wajah se, AI models galtiyan kar sakte hain. Ek neural network probabilities return karta hai, aur humein decisions lete waqt ise dhyaan mein rakhna chahiye. Har model ki kuch accuracy aur recall hoti hai, aur humein samajhna hoga ki galat advice se hone wale nuksaan ko kaise roka jaye.
* **Privacy aur Security** ke kuch AI-specific implications hote hain. Jaise, jab hum kisi model ko train karne ke liye kuch data use karte hain, toh yeh data kisi na kisi roop mein model mein "integrate" ho jaata hai. Ek taraf, yeh security aur privacy badhata hai, doosri taraf - humein yaad rakhna chahiye ki model ko kis data par train kiya gaya tha.
* **Inclusiveness** ka matlab hai ki hum AI ko logon ki jagah lene ke liye nahi bana rahe, balki logon ko augment karne aur hamare kaam ko zyada creative banane ke liye bana rahe hain. Yeh fairness se bhi related hai, kyunki jab under-represented communities ke saath deal karte hain, toh hum jo zyadatar datasets collect karte hain woh shayad biased hote hain, aur humein yeh sunishchit karna chahiye ki un communities ko include kiya jaye aur AI unhe sahi tareeke se handle kare.
* **Transparency**. Isme yeh sunishchit karna shaamil hai ki hum hamesha clear rahein ki AI use kiya ja raha hai. Iske alawa, jahan bhi possible ho, hum aise AI systems use karna chahte hain jo *interpretable* hon.
* **Accountability**. Jab AI models kuch decisions lete hain, toh hamesha clear nahi hota ki un decisions ke liye kaun responsible hai. Humein yeh sunishchit karna chahiye ki hum samajhte hain ki AI decisions ki responsibility kahan hai. Zyadatar cases mein hum important decisions lene ki process mein humans ko include karna chahenge, taaki asli logon ko accountable thehraya ja sake.

## Responsible AI ke liye Tools

Microsoft ne [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) develop kiya hai jisme tools ka ek set shaamil hai:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard jisme shaamil hain:

   - EconML - Causal Analysis ke liye tool, jo "what-if" sawaalon par focus karta hai
   - DiCE - Counterfactual Analysis ke liye tool jo aapko yeh dekhne deta hai ki model ke decision ko affect karne ke liye kin features ko change karna padega

AI Ethics ke baare mein zyada jaankari ke liye, kripya Machine Learning curriculum mein [is lesson](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) par jaiye jisme assignments shaamil hain.

## Review & Self Study

Responsible AI ke baare mein aur jaanne ke liye is [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) ko lijiye.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
