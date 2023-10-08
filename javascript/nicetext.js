function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function nicetext() {
  for (let i = 0; i < text.length; i++) {
    process.stdout.write(text[i]);
    await delay(25);
  }
}

const text = "nice text\n";
nicetext(text);
