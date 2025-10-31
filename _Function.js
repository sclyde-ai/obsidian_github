import fs from 'fs/promises';
import matter from 'gray-matter'; 
import { readdir } from 'fs/promises';
import { join } from 'path';

async function overwriteFrontmatter(file_path, new_frontmatter) {
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

async function changeFrontmatter(file_path, new_frontmatter) {
  try {
    const fileContentToRead = await fs.readFile(file_path, 'utf-8');

    const { previous_frontmatter, content } = matter(fileContentToRead);

    const fileContentToWrite = matter.stringify(content, new_frontmatter);

    await fs.writeFile(file_path, fileContentToWrite);

  } catch (err) {
    console.error('error:', err);
  }
}

async function removeFrontmatter(file_path) {
  try {
    const fileContent = await fs.readFile(file_path, 'utf-8');

    const { content } = matter(fileContent);

    await fs.writeFile(file_path, content);

  } catch (err) {
    console.error('error:', err);
  }
}