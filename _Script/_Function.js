import fs from 'fs/promises';
import matter from 'gray-matter'; 
import { readdir } from 'fs/promises';
import { join } from 'path';

export async function overwriteFrontmatter(file_path, new_frontmatter) {
  try {
    const fileContentToRead = await fs.readFile(file_path, 'utf-8');

    const { frontmatter, content } = matter(fileContentToRead);

    for (const key in new_frontmatter) {
      frontmatter[key] = new_frontmatter[key];
    }

    const fileContentToWrite = matter.stringify(content, frontmatter);

    await fs.writeFile(file_path, fileContentToWrite);

  } catch (err) {
    console.error('error:', err);
  }
}

export async function changeFrontmatter(file_path, new_frontmatter) {
  try {
    const fileContentToRead = await fs.readFile(file_path, 'utf-8');

    const { previous_frontmatter, content } = matter(fileContentToRead);

    const fileContentToWrite = matter.stringify(content, new_frontmatter);

    await fs.writeFile(file_path, fileContentToWrite);

  } catch (err) {
    console.error('error:', err);
  }
}

export async function removeFrontmatter(file_path) {
  try {
    const fileContent = await fs.readFile(file_path, 'utf-8');

    const { content } = matter(fileContent);

    await fs.writeFile(file_path, content);

  } catch (err) {
    console.error('error:', err);
  }
}

export async function getFilesRecursively(dirPath) {
  let filePaths = [];
  
  try {
    // ディレクトリ内のエントリ（ファイルやサブディレクトリ）を取得
    // withFileTypes: true にすると、fs.Dirent オブジェクトの配列が返る
    const entries = await readdir(dirPath, { withFileTypes: true });

    // console.log(entries)

    for (const entry of entries) {
      const fullPath = join(dirPath, entry.name);

      if (entry.isDirectory()) {
        // エントリがディレクトリなら、再帰的にスキャン
        const subDirFiles = await getFilesRecursively(fullPath);
        filePaths = filePaths.concat(subDirFiles);
      } else if (entry.isFile()) {
        // エントリがファイルなら、配列に追加
        filePaths.push(fullPath);
      }
    }
  } catch (err) {
    console.error(`Error reading directory ${dirPath}:`, err);
  }

  return filePaths;
}