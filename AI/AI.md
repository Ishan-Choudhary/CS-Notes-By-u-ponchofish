# AI
! There aren't enough past paper questions to cover the entire syllabus content !

## Graphs
A structure used to model relationships between objects
**Use in AI (9618/33/M/J/21)**
- Artificial neural networks can be represented with graphs
- Graphs show relationships between nodes
- AI problems can be framed as finding a path in a graph
- Graphs may be analysed by algorithms like Dijkstra's or A*

## Dijkstra's Algorithm and A* Algorithm
- Both are used to find the shortest path between two points
https://www.youtube.com/watch?v=EFg3u_E6eHU – Dijkstra's Algorithm, good video
https://www.youtube.com/watch?v=71CEj4gKDnE&t=12s – A*

A* is just Dijkstra's but a "heuristic" value is added to the distance value.

## Machine Learning
### Data
! No questions for this yet
Raw data must be manipulated to be useful
1. Data is transformed, e.g. if example in data set has 1 of 5 colours associated with it, word for the colour can be replaced with number
2. Data scrubbing. Examples with extreme data values/outliers and incomplete examples are removed from the data set.
3. Data is modelled with techniques explained below

### Categories of Learning
**Supervised**
- Using known tasks with known outcomes to enable a computer program to improve its performance in accomplishing similar tasks. (9618/03/SP/21)
- Or, according to Wikipedia and everybody else, a type of learning where each training example has an associated correct output label

**Unsupervised**
- Using a large number of tasks with unknown outcomes to enable a computer program to improve its performance in accomplishing similar tasks
- (and again, or a type of learning where input data is not associated with correct output labels)

**Reinforcement learning**
- Using a large number of tasks with unknown outcomes and the use of feedback to enable a computer program to improve its performance in accomplishing similar tasks
- (Type of learning where feedback on performance of model (usually "agent" in the context of reinforcement learning) is provided by the environment instead of concrete output labels)

### Artificial Neural networks
**How do machine learning with ANN's? (9618/32/O/N/21)**
- Modelled on the brain
- Weights are assigned to connections between nodes
- Data are input to the input layer
- Data analysed at each layer and features extracted
- Output layer outputs the result
- Weights are changed to reduce error by process of backpropagation
- Process of training repeated many times

**Why use many layers? (9618/32/O/N/21)**
- Enables deep learning to take place
- Many layers are required to solve complex problems
- To improve accuracy
- To enable the neural network to learn and make decisions on its own

### Linear regression 
! No questions for this yet
A statistical technique in which an attempt is made to fit a straight line to a data set.
### Logistic regression
! No questions for this yet
A statistical technique in which an attempt is made to fit a decision boundary to a data set that would allow the model to classify examples into 1 of 2 categories if you apply logistic regression 1 time since logistic function outputs a value from the continuous range between 0 and 1.
