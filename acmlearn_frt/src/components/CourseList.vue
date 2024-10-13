<template>
  <el-card>
    <el-row>
      <el-col :span="8">
        <el-select v-model="selectedCategory" placeholder="选择类别" @change="handleCategoryChange">
          <el-option
            v-for="category in categories"
            :key="category.id"
            :label="category.name"
            :value="category.id"
          />
        </el-select>
      </el-col>
      <el-col :span="8">
        <el-select v-model="selectedDifficulty" placeholder="选择难度" @change="handleDifficultyChange">
          <el-option
            v-for="difficulty in difficulties"
            :key="difficulty.id"
            :label="difficulty.name"
            :value="difficulty.id"
          />
        </el-select>
      </el-col>
      <el-col :span="8">
        <el-select v-model="selectedKnowledgePoint" placeholder="选择知识点" @change="handleKnowledgePointChange">
          <el-option
            v-for="knowledgePoint in knowledgePoints"
            :key="knowledgePoint.id"
            :label="knowledgePoint.name"
            :value="knowledgePoint.id"
          />
        </el-select>
      </el-col>
    </el-row>
    <el-row style="margin-top: 20px;">
      <el-col>
        <el-tag
          v-for="(tag, index) in selectedTags"
          :key="index"
          closable
          @close="removeTag(tag)"
        >
          {{ tag.label }}
        </el-tag>
      </el-col>
    </el-row>
    <el-row style="margin-top: 20px;">
      <el-col>
        <el-table :data="filteredCourses" style="width: 100%">
          <el-table-column prop="name" label="课程名称" />
          <el-table-column prop="category" label="类别" />
          <el-table-column prop="difficulty" label="难度" />
          <el-table-column prop="knowledgePoint" label="知识点" />
        </el-table>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  data() {
    return {
      selectedCategory: '',
      selectedDifficulty: '',
      selectedKnowledgePoint: '',
      categories: [
        { id: '1', name: '编程' },
        { id: '2', name: '设计' },
        { id: '3', name: '市场营销' },
      ],
      difficulties: [
        { id: '1', name: '初级' },
        { id: '2', name: '中级' },
        { id: '3', name: '高级' },
      ],
      knowledgePoints: [
        { id: '1', name: 'JavaScript' },
        { id: '2', name: 'HTML/CSS' },
        { id: '3', name: 'UI设计' },
        { id: '4', name: 'SEO' },
      ],
      courses: [
        { name: 'JavaScript基础', category: '编程', difficulty: '初级', knowledgePoint: 'JavaScript' },
        { name: 'HTML/CSS入门', category: '编程', difficulty: '初级', knowledgePoint: 'HTML/CSS' },
        { name: 'UI设计基础', category: '设计', difficulty: '中级', knowledgePoint: 'UI设计' },
        { name: 'SEO优化', category: '市场营销', difficulty: '高级', knowledgePoint: 'SEO' },
      ],
      selectedTags: [],
    };
  },
  computed: {
    filteredCourses() {
      return this.courses.filter(course => {
        const categoryMatch = !this.selectedCategory || course.category === this.selectedCategory;
        const difficultyMatch = !this.selectedDifficulty || course.difficulty === this.selectedDifficulty;
        const knowledgePointMatch = !this.selectedKnowledgePoint || course.knowledgePoint === this.selectedKnowledgePoint;
        return categoryMatch && difficultyMatch && knowledgePointMatch;
      });
    },
  },
  methods: {
    handleCategoryChange() {
      this.addTag('category', this.selectedCategory);
      this.selectedDifficulty = '';
      this.selectedKnowledgePoint = '';
    },
    handleDifficultyChange() {
      this.addTag('difficulty', this.selectedDifficulty);
      this.selectedKnowledgePoint = '';
    },
    handleKnowledgePointChange() {
      this.addTag('knowledgePoint', this.selectedKnowledgePoint);
    },
    addTag(type, value) {
      const label = this.getLabel(type, value);
      if (label) {
        this.selectedTags.push({ type, value, label });
      }
    },
    removeTag(tag) {
      this.selectedTags = this.selectedTags.filter(t => t !== tag);
      if (tag.type === 'category') {
        this.selectedCategory = '';
      } else if (tag.type === 'difficulty') {
        this.selectedDifficulty = '';
      } else if (tag.type === 'knowledgePoint') {
        this.selectedKnowledgePoint = '';
      }
    },
    getLabel(type, value) {
      if (type === 'category') {
        return this.categories.find(c => c.id === value)?.name;
      } else if (type === 'difficulty') {
        return this.difficulties.find(d => d.id === value)?.name;
      } else if (type === 'knowledgePoint') {
        return this.knowledgePoints.find(k => k.id === value)?.name;
      }
      return null;
    },
  },
};
</script>

<style scoped>
/* 添加一些样式 */
.el-card {
  margin: 20px;
}
.el-tag {
  margin-right: 10px;
  margin-bottom: 10px;
}
</style>