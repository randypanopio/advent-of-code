import fs from 'node:fs';


export function processInputFileAny(file_path: string) {
    try {
        return fs.readFileSync(file_path, 'utf8');
    } catch (err) {
        console.error(err);
    }
}

export function processInputFile(file_path: string): string[] {
    try {
        const fileContent = fs.readFileSync(file_path, 'utf8');
        return fileContent.split('\n');
    } catch (err) {
        console.error(err);
        return []; // Return an empty array in case of an error
    }
}
