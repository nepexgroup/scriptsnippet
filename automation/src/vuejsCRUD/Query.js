// mixins/Query.js
import {http} from '@/axios'

export const requestsMixin = {
    methods: {
        getBatches() {
            return http.get(`batches`);
        },
        // getProducts() {
        //     return global.axios.get(`products`);
        // },
        // getCategories() {
        //     return global.axios.get(`/categories`);
        // },
        // searchJokes(query) {
        //     return global.axios.get(`/search?query=${query}`);
        // }
    }
};
