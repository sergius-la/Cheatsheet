# Java - Data conversion

***

##### int -> String

```java
> Convert using new Integer(int).toString()
int number = 193_019;
String numberString = Integer.toString(number);

> Convert using String.format()
int number = -782;
String numberAsString = String.format ("%d", number);
```

***

##### String[] -> Set<String>

```java
String [] countries = {"India", "Switzerland", "Italy", "India"}; 
Set<String> set = new HashSet<String>(Arrays.asList(countries));
```

***

##### char[] -> String

```java
char[] data = {'a', 'b', 'c'};
String text = String.valueOf(data);
```

##int[]

***

##### int[] -> String

```java
int[] x = new int[] {3,4,5};
String s = Arrays.toString(x).replaceAll("[\\,\\[\\]\\ ]", "")

String s = IntStream.of(x)
  .mapToObj(Integer::toString)
  .collect(Collectors.joining(""));
```
***

##### int[] -> Integer[]

```java
int[] arr = {0, 1, 1, 1, 1 ,1 , 1, 33, 4, 43, 54, 32, 32, 32 , 54, 23, 55};
Integer[] intFirst = Arrays.stream( arr ).boxed().toArray( Integer[]::new );
```













