# Apriori_Generating_FrequentItemsets
Libraries used:
<ul>
  <li>Pandas Library: Used to manipulate the dataframe.</li>
  <li>Machine Learning Extended Library: Provides Apriori algorithm to generate association rules for extracting Frequent Itemsets.</li>
</ul>

Given dataset:

<blockquote>dataset =<br></br>
           [['Milk', 'Onion', 'Bread', 'Cheese', 'Cereals', 'Yogurt'],<br></br>
           ['Oil', 'Onion', 'Bread', 'Cheese', 'Cereals', 'Yogurt'],<br></br>
           ['Milk', 'Orange', 'Cheese', 'Cereals'],<br></br>
           ['Milk', 'Eggs', 'Corn', 'Cheese', 'Yogurt'],<br></br>
           ['Corn', 'Onion', 'Cheese', 'Ice cream', 'Cereals']]<br></br>
</blockquote>

Analyzing data for:
<blockquote>
  <ul>
    <li> Display associations rules for metric = 'lift' and min_threshold = 1.2 </li>
    <li> Display associations rules for metric = 'support' and min_threshold = 0.6 </li>
    <li> At least 2 antecedents and confidence greater than or equal to 0.75 </li>
    <li> Support atleast 0.8 and lift atleast 1.00 </li>
    <li> Sort the rules in descending order first by length of antecedents and then by lift </li>
  </ul>
</blockquote>

Results:
<img src="https://github.com/gabrielleviray/Apriori_Generating_FrequentItemsets/blob/master/apriori_1.JPG" </img>
          
         
