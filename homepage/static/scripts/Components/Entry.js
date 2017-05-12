class BlogEntry extends HTMLElement {
  constructor() {
    super();
  }

  static get observedAttributes() {return ['data-entry-id']; }

  attributeChangedCallback(attr, oldValue, newValue) {
    if (attr == 'data-entry-id') {
      var xhr = new XMLHttpRequest;
      var entryContent;
      xhr.onreadystatechange = function() {
        entryContent = JSON.parse(xhr.responseText);
        console.log(entryContent);
        var r = document.querySelector("#root")
        var blogEntry = document.querySelector("#blog-1")
        blogEntry.textContent = entryContent['body_raw'];
      }
      xhr.open("GET", `/api/entries/${newValue}`);
      xhr.send();
    }
  }
}
customElements.define('blog-entry', BlogEntry)
