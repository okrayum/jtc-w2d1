// Book info object was created with ChatGPT. Prompt = create me a book info object const bookInfo = {} about the book Dune, with a short synopsis

const bookInfo = {
  title: "Dune",
  author: "Frank Herbert",
  genre: "Science Fiction",
  publicationYear: 1965,
  publisher: "Chilton Books",
  pageCount: 412,
  synopsis: "Dune is a science fiction novel set in a distant future where noble families control planets. It follows the story of Paul Atreides as his family gains control of the desert planet Arrakis, the only source of a valuable substance called 'spice'. The novel explores themes of politics, religion, ecology, and human emotion.",
  rating: 4.35 // Example rating (out of 5)
};

const serializedBookInfo = JSON.stringify(bookInfo);

console.log(serializedBookInfo);