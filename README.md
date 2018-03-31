# SOP_KMAP_DRAW
This program takes a SOP type argument and draws it as a K-Map.

## What is Sum of Products (SOP)?

In Boolean algebra, any Boolean function can be put into the canonical disjunctive normal form (CDNF) or minterm canonical form and its dual canonical conjunctive normal form (CCNF) or maxterm canonical form. Other canonical forms include the complete sum of prime implicants or Blake canonical form (and its dual), and the algebraic normal form (also called Zhegalkin or Reed–Muller).

Minterms are called products because they are the logical AND of a set of variables, and maxterms are called sums because they are the logical OR of a set of variables. These concepts are dual because of their complementary-symmetry relationship as expressed by De Morgan's laws.

Two dual canonical forms of any Boolean function are a "sum of minterms" and a "product of maxterms." The term "Sum of Products" or "SoP" is widely used for the canonical form that is a disjunction (OR) of minterms. Its De Morgan dual is a "Product of Sums" or "PoS" for the canonical form that is a conjunction (AND) of maxterms. These forms can be useful for the simplification of these functions, which is of great importance in the optimization of Boolean formulas in general and digital circuits in particular.


## What is Karnaugh Map (K-Map)?

The Karnaugh map (KM or K-map) is a method of simplifying Boolean algebra expressions. Maurice Karnaugh introduced it in 1953 as a refinement of Edward Veitch's 1952 Veitch chart, which actually was a rediscovery of Allan Marquand's 1881 logical diagram. aka Marquand diagram but with a focus now set on its utility for switching circuits. Veitch charts are therefore also known as Marquand–Veitch diagrams, and Karnaugh maps as Karnaugh–Veitch maps (KV maps).

The Karnaugh map reduces the need for extensive calculations by taking advantage of humans' pattern-recognition capability. It also permits the rapid identification and elimination of potential race conditions.

The required Boolean results are transferred from a truth table onto a two-dimensional grid where, in Karnaugh maps, the cells are ordered in Gray code, and each cell position represents one combination of input conditions, while each cell value represents the corresponding output value. Optimal groups of 1s or 0s are identified, which represent the terms of a canonical form of the logic in the original truth table. These terms can be used to write a minimal Boolean expression representing the required logic.

Karnaugh maps are used to simplify real-world logic requirements so that they can be implemented using a minimum number of physical logic gates. A sum-of-products expression can always be implemented using AND gates feeding into an OR gate, and a product-of-sums expression leads to OR gates feeding an AND gate. Karnaugh maps can also be used to simplify logic expressions in software design. Boolean conditions, as used for example in conditional statements, can get very complicated, which makes the code difficult to read and to maintain. Once minimised, canonical sum-of-products and product-of-sums expressions can be implemented directly using AND and OR logic operators.


## Result

### 1-Variable Karnaugh Map

![1.JPG]({{site.baseurl}}/1.JPG)

### 2-Variable Karnaugh Map

![2.JPG]({{site.baseurl}}/2.JPG)

### 3-Variable Karnaugh Map

![3.JPG]({{site.baseurl}}/3.JPG)

### 4-Variable Karnaugh Map

![4.JPG]({{site.baseurl}}/4.JPG)

