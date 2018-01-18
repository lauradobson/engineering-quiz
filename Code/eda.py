import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')


'''''
df_gender.work_outfit
df_gender.start_work
df_gender.design_something
df_gender.analyze_something
df_gender.solve_problem
df_gender.prefer_to
df_gender.work_partof
df_gender.on_project
df_gender.care_most
df_gender.goals
df_gender.eavesdrop
df_gender.develop_skills
df_gender.working_with
df_gender.leader
'''''

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.happy, data=df_gender, hue="gender")
plt.title('Are you happy in your program?')
plt.xlabel("Happy")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('happy.png', bbox_inches='tight')
plt.close()


# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.field_interest, data=df_gender, hue="gender")
plt.title('Field of Interest?')
plt.xlabel("Field of Interest")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('field_interest.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.team_responsible, data=df_gender, hue="gender")
plt.title('Would you want to be on the team responsible for?')
plt.xlabel("Team Responsible for")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('team_responsible.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.dream_professor, data=df_gender, hue="gender")
plt.title('Who is your Dream Professor?')
plt.xlabel("Dream Professor")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('dream_professor.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.work_setting, data=df_gender, hue="gender")
plt.title('What is your ideal work setting?')
plt.xlabel("Work Setting")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('work_setting.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.start_work, data=df_gender, hue="gender")
plt.title('You want to work for?')
plt.xlabel("Start work")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('start_work.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.design_something, data=df_gender, hue="gender")
plt.title('You would rather design')
plt.xlabel("Design Something")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('design_something.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.analyze_something, data=df_gender, hue="gender")
plt.title('You would rather analyze?')
plt.xlabel("Analyze Something")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('analyze_something.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.solve_problem, data=df_gender, hue="gender")
plt.title('You would rather solve the problem:')
plt.xlabel("Solve Problem")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('solve_problem.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.prefer_to, data=df_gender, hue="gender")
plt.title('You prefer to')
plt.xlabel("Prefer To")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('prefer_to.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.work_partof, data=df_gender, hue="gender")
plt.title('You want to work apart of:')
plt.xlabel("Work Apart Of")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('work_partof.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.on_project, data=df_gender, hue="gender")
plt.title('You want to be on a project that')
plt.xlabel("Project")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('on_project.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.care_most, data=df_gender, hue="gender")
plt.title('You Care most about')
plt.xlabel("Care Most")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('care_most.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.goals, data=df_gender, hue="gender")
plt.title('You Set Goals...')
plt.xlabel("Goals")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('goals.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.eavesdrop, data=df_gender, hue="gender")
plt.title('You Would Eavesdrop in a Conversation Regarding')
plt.xlabel("Eavesdrop")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('eavesdrop.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.develop_skills, data=df_gender, hue="gender")
plt.title('You want to develop skills in')
plt.xlabel("Develop Skills")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('develop_skills.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.working_with, data=df_gender, hue="gender")
plt.title('You want to work with')
plt.xlabel("Work with")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('working_with.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_gender=pd.read_csv('eng_gender.csv',encoding='cp1252')
sns.countplot(df_gender.leader, data=df_gender, hue="gender")
plt.title('Do you want to be a leader?')
plt.xlabel("Leader")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('leader.png', bbox_inches='tight')
plt.close()

# BAR CHART
df_no=pd.read_csv('eng_no.csv',encoding='cp1252')
sns.countplot(df_no.year, data=df_no)
plt.title('What Year Are You In?')
plt.xlabel("Computer Engineer Year")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.savefig('year_comp.png', bbox_inches='tight')
plt.close()