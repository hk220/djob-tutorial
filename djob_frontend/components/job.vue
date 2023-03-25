<script setup>
const props = defineProps({
    my: {
        type: [Boolean]
    },
    job: {
        type: [Object]
    }
})
</script>

<template>
    <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
        <div>
            <h2 class="mb-2 text-xl font-semibold">{{ job.title }}</h2>
            <p class="text-gray-600">{{ job.company_name }}</p>
        </div>
        <div>
            <p class="mb-2">{{ job.position_location }}</p>
            <p>{{ job.position_salary }}</p>
        </div>

        <div>
            <p>{{  job.created_at_formatted }}</p>

        </div>

        <div class="space-x-4">
            <NuxtLink v-bind:to="'/browse/' + job.id" class="py-4 px-6 bg-teal-700 text-white rounded-xl">Details</NuxtLink>
            <NuxtLink to="/browse/1" class="py-4 px-6 bg-cyan-700 text-white rounded-xl" v-if="my">Edit</NuxtLink>
            <NuxtLink to="/browse/1" class="py-4 px-6 bg-rose-700 text-white rounded-xl" v-if="my">Delete</NuxtLink>
        </div>
    </div>
</template>