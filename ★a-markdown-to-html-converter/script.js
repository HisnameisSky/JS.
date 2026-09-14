function convertMarkdown() {
  const markdownInput = document.getElementById("markdown-input");
  let text = markdownInput ? markdownInput.value : "";

  text = text.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img alt="$1" src="$2">');

  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

  text = text.replace(/^[ \t]*### (.*)$/gm, '<h3>$1</h3>');
  text = text.replace(/^[ \t]*## (.*)$/gm, '<h2>$1</h2>');
  text = text.replace(/^[ \t]*# (.*)$/gm, '<h1>$1</h1>');

  text = text.replace(/^[ \t]*> (.*)$/gm, '<blockquote>$1</blockquote>');

  text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/__(.*?)__/g, '<strong>$1</strong>');

  text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
  text = text.replace(/_(.*?)_/g, '<em>$1</em>');

  const htmlResult = text.replace(/\n/g, '');

  return htmlResult;
}

const markdownInputElem = document.getElementById("markdown-input");
const htmlOutputElem = document.getElementById("html-output");
const previewElem = document.getElementById("preview");

if (markdownInputElem) {
  markdownInputElem.addEventListener("input", () => {
    const html = convertMarkdown();
    
    if (htmlOutputElem) {
      htmlOutputElem.textContent = html;
    }
    
    if (previewElem) {
      previewElem.innerHTML = html;
    }
  });
}

/*imp*/

const markdownInput = document.getElementById("markdown-input");
const preview = document.getElementById("preview");

if(markdownInput && preview){
    let isMarkdownHovered=false;
    let isPreviewHovered = false;

    markdownInput.addEventListener("mouseenter",()=>{
        isMarkdownHovered=true;
    });
    markdownInput.addEventListener("mouseleave",()=>{
        isMarkdownHovered=false;
    });
    preview.addEventListener("mouseenter",()=>{
        isPreviewHovered=true;
    });
    preview.addEventListener("mouseleave",()=>{
        isPreviewHovered=false;
    });

    markdownInput.addEventListener("scroll",()=>{
        if(isMarkdownHovered){
            const maxScrollInput=markdownInput.scrollHeight-markdownInput.clientHeight;
            const maxScrollPreview = preview.scrollHeight-preview.clientHeight;

            if(maxScrollInput > 0){
                const scrollRatio = markdownInput.scrollTop / maxScrollInput;
                preview.scrollTop=scrollRatio * maxScrollPreview;
            }
        }
    });

    preview.addEventListener("scroll", () => {
    if (isPreviewHovered) {
      const maxScrollInput = markdownInput.scrollHeight - markdownInput.clientHeight;
      const maxScrollPreview = preview.scrollHeight - preview.clientHeight;

      if (maxScrollPreview > 0) {
        const scrollRatio = preview.scrollTop / maxScrollPreview;
        markdownInput.scrollTop = scrollRatio * maxScrollInput;
      }
    }
  });
}