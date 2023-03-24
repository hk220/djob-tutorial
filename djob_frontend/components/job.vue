<script setup>
const props = defineProps({
    my: {
        type: [Boolean]
    }
})
</script>

<template>
    <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
        <div>
            <h2 class="mb-2 text-xl font-semibold">The job position</h2>
            <p class="text-gray-600">The company name</p>
        </div>
        <div>
            <p class="mb-2">Worldwide</p>
            <p>$90-120k</p>
        </div>

        <div>
            <p>Posted Dec. 1. 2022</p>

        </div>

        <div class="space-x-4">
            <NuxtLink to="/browse/1" class="py-4 px-6 bg-teal-700 text-white rounded-xl">Details</NuxtLink>
            <NuxtLink to="/browse/1" class="py-4 px-6 bg-cyan-700 text-white rounded-xl" v-if="my">Edit</NuxtLink>
            <NuxtLink to="/browse/1" class="py-4 px-6 bg-rose-700 text-white rounded-xl" v-if="my">Delete</NuxtLink>
        </div>
    </div>
</template>