## Simplexes on vector representations of words


While tSNE is a powerful tool for dimensionality reduction, when employed on language models to create two dimensional representations, it often fails to fully capture different dimensions of meaning. Past approaches by [Lauren Van Der Maaten](https://lvdmaaten.github.io/multiplemaps/Multiple_maps_t-SNE/Multiple_maps_t-SNE_files/fulltext.pdf) (Multiple Map) to reveal complementary structure have sidestepped the main problem, the different contexts in which a word can appear.

Here, an alternative approach has been implemented that uses simplices to reveal multiple planes of meaning. By looking at the planes of a simplex, we can determine the different contexts in which a certain word(/point/vertex) might fit. Also, by looking at the vertices of a simplex, we get what might actually be good poetry.

### Methodology

Okay, when I say simplex, I mean tetrahedron, the most intuitive representation, and the only one that I've implemented so far. Using a filtered word2vec embedding of 44k words, we still apply tSNE to the word2vec embedding, but instead of reducing it to 2 dimensions, we reduce it to 3 dimensions. 

Starting at an arbitrary point, we then find four equidistant vertices that are spaced equally apart. Each of these four vertices is now at the intersection of three planes (contexts, dimensions etc.) of meaning. By removing any vertex from the four, we can obtain a plane/context/dimension. 

Through this approach, we can avoid the triangle inequality problem that is prevalent in 2D tSNE maps. To use the example from Maaten's Tech Talk, a word like "bank" is related to "river" but also to "bailout". This might lead "river" and "bailout" to be represented as close together, when in fact they are not similar. By representing this original triangle as distinct points in three dimensions, we see that the word "bank" is a vertex on two separate planes of meaning, one having to do with the land along the edge of a river, and the other with financial institutions. These two planes/contexts of meaning are basically perpendicular (having nothing to do with one another).

![separate planes of meaning in 3d tsne embedding](https://www.eric-xia.com/images/ghsimplex.png)

*This is from the filtered word2vec embedding. The two planes shown here contain (A,B,C) and (A,E,H), and the angle between them is ~89 degrees.*

Okay, so three dimensional representations can reveal planes or contexts of meaning that can't be seen in two dimensions. Now what about the tetrahedron? 

I came up with this idea while prompt-engineering for word golf. I wanted to find polysemous words which would surprise the user; like how *kindling* is both related to  *curiosity* and *flame*, or how *star* is related to *sky* and *actor*. These words would be at the intersection of different planes of meaning. One way to do this is to look at the vertices of a regular tetrahedron.

Here are some results so far:

Poem #1
> jumps token stares interjections

Poem #2
> similarity dying signals endured

Poem #3
> flopping persona conundrum blades

Poem #4
> granite african liftoff sooner

...
>autonomy excessively prophesied consistently

> souvenirs tangling divisional scarcely

>inexorable frau overthrows watchmakers

>monument souvenirs bridge jar

>desirous resemble collecting costed

>bedside talley borrowing locking

>habits horrors unscientific tarnish

>confessional convex tackle treasuries

>underlines meeting vigil ignorant

>incentives parolee droppings neuroticism

>shoulders chimney sunroof jobseekers

>esoteric organs tornadoes rope

>conscientiousness hall givens ticker

>comms technique pyrotechnic solute

Because these words are equally separated in space, they have no meaning taken as a whole. In other words, there is no "category" into which you could place all four words (try to do it!). But looking at each of the four sets of three evokes the gentlest of patterns. 

The tetrahedron is an elegant kind of poetry, almost a haiku, and it is completely computationally generated.

## How to Use

Run `tetrahedron.py` to search for and log words in tetrahedron-like formations. It first searches by distance for four points which are around the same distance from the start point, and then checks those points for their crossdistances.

