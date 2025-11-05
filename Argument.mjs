import { readdir } from 'fs/promises';
import { join } from 'path';

export async function combinePath(path_list){
    let path = path_list[0]
    for (const name of path_list.slice(1, path_list.length)) {
      path += ' '
      path += name
    }
    return path
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

// export {combinePath, getFilesRecursively};