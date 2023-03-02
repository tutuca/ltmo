const { resolve, parse, basename } = require("path");
const glob = require("glob");


function getEntries() {
    const matches = glob.sync("./assets/views/**/index.js");

    const entries = Object.fromEntries(matches.map(f => {
        const { dir } = parse(f);
        const entry = basename(dir);
        return [entry, f];
    }));

    const out =  {
        stylesheet: resolve("./assets/scss/style.scss"),
        main: resolve("./assets/main.js"),
        ...entries
    };

    return out
}

const rollupOptions = {

    input: getEntries(),

    output: {
        entryFileNames: "[name].js",
        chunkFileNames: undefined,
        assetFileNames: '[name][extname]'

    },
};

module.exports = {
    plugins: [],
    root: resolve("./src"),
    base: "/static/",
    resolve: {
        extensions: [".js", ".json"],
    },
    build: {
        outDir: resolve("./ltmo/static/"),
        target: "es2015",
        sourcemap: true,
        rollupOptions
    },
};
