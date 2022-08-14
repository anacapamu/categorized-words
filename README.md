# Categorized Words

Categorized Words is an API that returns words of a category. 

## Endpoints
### GET
`[/categories]` reads all categories<br/>
`[/words]` reads all words<br/>
`[/categories/<category_id>/words]` reads all words for specified category<br/>

### POST
`[/categories]` creates a category<br/>
`[/categories/<category_id>/words]` creates a word for specified category<br/>

### DELETE
`[/categories/<category_id>]` deletes specified category<br/>
`[/words/<word_id>]` deletes specified word<br/>

### PATCH
`[/words/<word_id>]` change category_id of word<br/>

