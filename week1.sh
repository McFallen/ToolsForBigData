# Exercise 1.1
echo 'Exercise 1.1'
tr ' ' '\n' < input/exercise1_1.txt | sort | uniq -c | sort -nr | grep -E -m10 ".*"

# Exercise 1.2
#echo ''
#echo 'Exercise 1.2'
#grep -E "^.*\s[0-9]{1,4}\n?$" input/exercise1_2.txt

# Exercise 1.3
#echo ''
#echo 'Exercise 1.3'
#tr ' ' '\n' < input/shakespeare.txt | tr -d '![]()|,.:;\t' | sort -u > output/shakespeare_dict; comm --nocheck-order input/dict output/shakespeare_dict | grep -cP "\t{2}"; rm output/shakespeare_dict
















