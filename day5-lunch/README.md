# QBB-Day 5-Lunch 

Exercise 1:
count the number of de novo mutations per proband : 26432

code done: 
sort aau1043_dnm.csv | uniq -c > sorted_aau1043_dnm.csv
awk 'BEGIN{FS="," ; OFS="\t"} {if ($6 == "father"){ print $5, $6}}' aau1043_dnm.csv | sort | uniq -c > father.txt
awk 'BEGIN{FS="," ; OFS="\t"} {if ($6 == "mother"){ print $5, $6}}' aau1043_dnm.csv | sort | uniq -c > mother.txt
join -1 2 -2 2 mother.txt father.txt |sort -n > parents_mut_count.txt
tail -n +2 aau1043_parental_age.csv > parent_age.csv
tr ',' ' ' <parent_age.csv > parent_age.txt # this got rid of the comma seperated values
 join -1 1 -2 1 parent_age.txt parents_mut_count.txt > parent_age_mut_count.txt
 
Exercise 3
code for graphs:

fig, ax = plt.subplots()
x = age_m
y = mut_count_m
ax.scatter(x, y, alpha = 0.4, label= "#of muts")
ax.set_xlabel("age")
ax.set_ylabel("# of de novo mutants")
ax.legend()
plt.savefig('ex2_a.png')
 
fig, ax = plt.subplots()
x2 = age_f
y2 = mut_count_f
ax.scatter(x2, y2, alpha = 0.4, label= "#of muts")
ax.set_xlabel("age")
ax.set_ylabel("# of de novo mutants")
ax.legend()
plt.savefig('ex2_b.png')

---

Relationship is significantly correlated based upon high p-value when coompared against using a ttest statistic. 
code used : print(stats.ttest_ind(age_m, mut_count_m))
Ttest_indResult(statistic=37.818940724941015, pvalue=2.8184672622190877e-179)








