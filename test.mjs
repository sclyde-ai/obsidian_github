// import fs from 'fs/promises';
// import matter from 'gray-matter'; 
// import { readdir } from 'fs/promises';
// import { join } from 'path';
import { removeFrontmatter } from "./_Script/Frontmatter.mjs";
import { combinePath, getFilesRecursively} from "./_Script/Argument.mjs";


(async () => {
  try {
      // console.log(process.argv);
    if (process.argv[2] == '-r') {
      const dirPath = await combinePath(process.argv.slice(3, process.argv.length));
      const allFiles = await getFilesRecursively(dirPath);

      for (const file of allFiles) {
        console.log(file);
        removeFrontmatter(file);
      } 
    }
    else if (process.argv[2] == '-f') {
      const filePath = await combinePath(process.argv.slice(3, process.argv.length));
      console.log(filePath);
      removeFrontmatter(filePath);
    }
    else {
      console.log("error: format is incorrect");
    }
  }
  catch (error) {
    console.log("error", error);
  }
})();