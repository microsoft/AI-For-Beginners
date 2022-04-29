src = 'questions-en.txt'
dst_dir = '../quiz-app/src/assets/translations/en'

import json,os
from copy import deepcopy

from matplotlib.cbook import ls_mapper

def mk_id(s): # convert from 4B/4E to numeric lesson id
    lesson_no = int(s[:-1])
    return lesson_no + (100 if s[-1]=='B' else 200)

with open('template.json') as f:
    doc = json.load(f)

inp = open(src,encoding='utf-8').readlines()

prev_q = None
prev_l = None
prev_l_id = None
lessons = { }

for l in inp:
    l = l.strip()
    if l=='': continue
    if l.startswith('+') or l.startswith('-'): # answer
        prev_q['answerOptions'].append({ "answerText" : l[2:], "isCorrect" :  l.startswith('+') })
    elif l.startswith('*'):
        if prev_q:
            prev_l['quiz'].append(prev_q)
        prev_q = { "questionText" : l[2:], "answerOptions" : [] };
    elif l.startswith('Lesson'):
        if prev_q:
            prev_l['quiz'].append(prev_q)
            prev_q = None
        if prev_l is not None:
            lessons[prev_l_id] = prev_l
        prev_l_id = l[7:l.find(' ',7)]
        prev_l = { "id" : mk_id(prev_l_id), "title" : l[l.find(' ',7)+1:], "quiz" : [] }
    else:
        print(f"Error: {l}")

prev_l['quiz'].append(prev_q)
lessons[prev_l_id] = prev_l

lesson_content = {}
for k,v in lessons.items():
    no = int(k[:-1])
    if no not in lesson_content.keys():
        lesson_content[no] = deepcopy(doc)
    lesson_content[no][0]['quizzes'].append(v)

with open(os.path.join(dst_dir,'index.js'),'w',encoding='utf-8') as f:
    for i,k in enumerate(lesson_content.keys()):
        f.write(f'import x{k} from "./lesson-{k}.json";\n')
    t = ', '.join([ f"{i} : x{k}[0]" for i,k in enumerate(lesson_content.keys())]);
    f.write(f"const quiz = {{ {t} }}; \n");
    f.write("export default quiz;")
    
for k,v in lesson_content.items():
    with open(os.path.join(dst_dir,f"lesson-{k}.json"),'w', encoding='utf-8') as f:
        json.dump(v,f,indent=2)
