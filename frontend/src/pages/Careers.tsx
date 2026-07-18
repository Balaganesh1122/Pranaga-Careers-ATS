import React, { useState, useMemo, useEffect, useRef } from "react";
import { 
  Search, 
  MapPin, 
  Briefcase, 
  ChevronLeft, 
  ChevronRight, 
  Check, 
  ShieldAlert, 
  Globe, 
  MessageCircle, 
  ArrowRight,
  Phone,
  MessageSquare,
  Award,
  Send,
  X,
  User,
  Mail,
  FileText,
  MessageSquareDiff,
  Info
} from "lucide-react";
import { jobsData, testimonialsData } from "../data/jobsData";

interface ChatMessage {
  sender: "user" | "bot";
  text: string;
}

const Careers: React.FC = () => {
  // State for job filters
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedDept, setSelectedDept] = useState("All");
  const [selectedLoc, setSelectedLoc] = useState("All");

  // State for modals
  const [isContactOpen, setIsContactOpen] = useState(false);
  const [isApplyOpen, setIsApplyOpen] = useState(false);
  const [selectedJobTitle, setSelectedJobTitle] = useState("");
  const [isCookieOpen, setIsCookieOpen] = useState(false);
  const [isAccessibilityOpen, setIsAccessibilityOpen] = useState(false);
  
  // Contact Form Inputs
  const [contactName, setContactName] = useState("");
  const [contactEmail, setContactEmail] = useState("");
  const [contactMessage, setContactMessage] = useState("");
  const [contactSuccess, setContactSuccess] = useState(false);

  // Application Form Inputs
  const [applyName, setApplyName] = useState("");
  const [applyEmail, setApplyEmail] = useState("");
  const [applyPortfolio, setApplyPortfolio] = useState("");
  const [applyFileName, setApplyFileName] = useState("");
  const [applySuccess, setApplySuccess] = useState(false);

  // AI Assistant Chat Widget State
  const [isChatOpen, setIsChatOpen] = useState(false);
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([
    { sender: "bot", text: "Hi! I am the Pranaga AI Assistant. Ask me anything about our job openings, team culture, or hiring process!" }
  ]);
  const [chatInput, setChatInput] = useState("");
  const [isBotTyping, setIsBotTyping] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll chat history to bottom
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chatMessages, isBotTyping]);

  // Get departments and locations dynamically for filter dropdowns
  const departments = useMemo(() => {
    const depts = jobsData.map((job) => job.department);
    return ["All", ...Array.from(new Set(depts))];
  }, []);

  const locations = useMemo(() => {
    const locs = jobsData.map((job) => job.location);
    return ["All", ...Array.from(new Set(locs))];
  }, []);

  // Filter jobs based on user input
  const filteredJobs = useMemo(() => {
    return jobsData.filter((job) => {
      const matchesSearch = 
        job.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        job.department.toLowerCase().includes(searchQuery.toLowerCase());
      
      const matchesDept = selectedDept === "All" || job.department === selectedDept;
      const matchesLoc = selectedLoc === "All" || job.location === selectedLoc;
      
      return matchesSearch && matchesDept && matchesLoc;
    });
  }, [searchQuery, selectedDept, selectedLoc]);

  // Testimonials Carousel Logic
  const [activeTestimonial, setActiveTestimonial] = useState(0);
  const handlePrevTestimonial = () => {
    setActiveTestimonial((prev) => 
      prev === 0 ? testimonialsData.length - 1 : prev - 1
    );
  };
  const handleNextTestimonial = () => {
    setActiveTestimonial((prev) => 
      prev === testimonialsData.length - 1 ? 0 : prev + 1
    );
  };

  useEffect(() => {
    const rotation = setInterval(() => {
      setActiveTestimonial((prev) => 
        prev === testimonialsData.length - 1 ? 0 : prev + 1
      );
    }, 4200);

    return () => clearInterval(rotation);
  }, []);

  // Life at Pranaga image
  const lifePhoto = { src: "/assets/rooftop_meeting.png", alt: "Team chatting on a rooftop terrace during sunset" };

  // Testimonials list for looping slider
  const sliderTestimonials = [
    testimonialsData[2], // David (index 0)
    testimonialsData[0], // Marcus (index 1)
    testimonialsData[1], // Sarah (index 2)
    testimonialsData[2], // David (index 3)
    testimonialsData[0], // Marcus (index 4)
  ];

  // AI Assistant message handler
  const handleSendChatMessage = (text: string) => {
    if (!text.trim()) return;

    // Add user message
    const newMessages = [...chatMessages, { sender: "user" as const, text }];
    setChatMessages(newMessages);
    setChatInput("");
    setIsBotTyping(true);

    // Simulate bot response after a brief delay
    setTimeout(() => {
      let botResponse = "I'm not sure about that, but feel free to apply or talk to a recruiter!";
      const lowerText = text.toLowerCase();

      if (lowerText.includes("benefit") || lowerText.includes("perk")) {
        botResponse = "We offer flexible hours ('Any Time'), remote-first workspace passes ('Work Anywhere') with coworking stipends, premium healthcare, and annual learning budgets.";
      } else if (lowerText.includes("culture") || lowerText.includes("life") || lowerText.includes("async")) {
        botResponse = "Our culture is focused on depth. We minimize meetings and prioritize async documentation, allowing you to focus on high-impact deep work.";
      } else if (lowerText.includes("hiring") || lowerText.includes("process") || lowerText.includes("interview")) {
        botResponse = "Our process is simple and transparent: 1. Application, 2. 30-minute introductory call, 3. Real-world collaborative task, 4. Job Offer!";
      } else if (lowerText.includes("job") || lowerText.includes("role") || lowerText.includes("openings")) {
        botResponse = "We currently have openings for a Senior Machine Learning Architect, Principal Product Designer, and more. Scroll to our 'Find your next challenge' section to search and apply!";
      }

      setChatMessages(prev => [...prev, { sender: "bot" as const, text: botResponse }]);
      setIsBotTyping(false);
    }, 800);
  };

  // Handle contact form submission
  const handleContactSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!contactName || !contactEmail || !contactMessage) return;
    setContactSuccess(true);
    setTimeout(() => {
      setContactSuccess(false);
      setIsContactOpen(false);
      setContactName("");
      setContactEmail("");
      setContactMessage("");
    }, 2500);
  };

  // Handle job application submission
  const handleApplySubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!applyName || !applyEmail) return;
    setApplySuccess(true);
    setTimeout(() => {
      setApplySuccess(false);
      setIsApplyOpen(false);
      setApplyName("");
      setApplyEmail("");
      setApplyPortfolio("");
      setApplyFileName("");
    }, 2500);
  };

  return (
    <div className="min-h-screen bg-[#F8FAFC] text-slate-900 font-sans selection:bg-blue-600 selection:text-white scroll-smooth">
      {/* HEADER */}
      <header className="fixed top-0 left-0 right-0 z-50 bg-white/90 backdrop-blur-md border-b border-slate-100">
        <div className="max-w-7xl mx-auto px-6 h-18 flex items-center">
          <nav className="flex items-center gap-8">
            <a href="#openings" className="text-[15px] font-semibold text-slate-900 relative py-1 after:absolute after:bottom-0 after:left-0 after:right-0 after:h-0.5 after:bg-blue-600">
              Careers
            </a>
          </nav>


        </div>
      </header>

      {/* HERO SECTION */}
      <section className="relative overflow-hidden pt-28 pb-24 md:pt-36 md:pb-32 bg-gradient-to-b from-white to-[#F8FAFC]">
        <div className="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          
          {/* Hero Content */}
          <div className="lg:col-span-7 flex flex-col items-start text-left z-10">
            <span className="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-full text-xs font-semibold tracking-wider text-blue-700 bg-blue-50 uppercase border border-blue-100 mb-6">
              JOIN THE REVOLUTION
            </span>
            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-[#0F172A] leading-[1.15] mb-6">
              Build the Future of <br />
              Human <br />
              Collaboration
            </h1>
            <p className="text-lg text-slate-500 max-w-xl leading-relaxed mb-10">
              At Pranaga, we're redesigning how teams think, plan, and execute using intelligence. Join our mission to augment human potential.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
              <a 
                href="#openings" 
                className="bg-[#0A66C2] hover:bg-blue-700 active:scale-98 text-white px-8 py-4 rounded-lg text-base font-semibold transition-all text-center"
              >
                View Openings
              </a>
              <button 
                onClick={() => setIsContactOpen(true)}
                className="bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 px-8 py-4 rounded-lg text-base font-semibold transition-all text-center active:scale-98 cursor-pointer"
              >
                Our Contact
              </button>
            </div>
          </div>

          {/* Hero Images Right */}
          <div className="lg:col-span-5 relative w-full flex justify-center lg:justify-end">
            <img 
              src="/assets/hero_right.png" 
              alt="Collaborative teamwork mockup" 
              className="w-full max-w-[500px] h-auto object-contain rounded-2xl drop-shadow-2xl"
            />
          </div>

        </div>
      </section>

      {/* JOB BOARD SECTION */}
      <section id="openings" className="py-24 bg-white border-t border-slate-100">
        <div className="max-w-4xl mx-auto px-6">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold tracking-tight text-slate-900 mb-4">
              Find your next challenge
            </h2>
            <p className="text-slate-500 text-lg">
              Search through our global opportunities in engineering, design, and product.
            </p>
          </div>

          {/* Filters Bar */}
          <div className="bg-white p-6 rounded-3xl border border-slate-100 shadow-sm flex flex-col md:flex-row gap-4 mb-8">
            <div className="flex-1 relative bg-[#F1F3F5] rounded-xl">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-500" />
              <input 
                type="text" 
                placeholder="Search roles, skills, or keywords" 
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-12 pr-4 py-4 bg-transparent rounded-xl focus:outline-none text-[15px] transition-all placeholder:text-slate-500 text-slate-800"
              />
            </div>

            <div className="flex gap-4">
              <div className="relative flex-1 md:w-36 bg-[#F1F3F5] rounded-xl flex items-center">
                <select 
                  value={selectedDept}
                  onChange={(e) => setSelectedDept(e.target.value)}
                  className="w-full appearance-none pl-4 pr-10 py-4 bg-transparent border-none focus:outline-none text-[15px] font-semibold text-slate-800 cursor-pointer"
                >
                  <option disabled value="">Department</option>
                  {departments.map((dept) => (
                    <option key={dept} value={dept}>{dept === "All" ? "Department" : dept}</option>
                  ))}
                </select>
                <div className="absolute right-4 pointer-events-none text-slate-500 text-xs">▼</div>
              </div>

              <div className="relative flex-1 md:w-32 bg-[#F1F3F5] rounded-xl flex items-center">
                <select 
                  value={selectedLoc}
                  onChange={(e) => setSelectedLoc(e.target.value)}
                  className="w-full appearance-none pl-4 pr-10 py-4 bg-transparent border-none focus:outline-none text-[15px] font-semibold text-slate-800 cursor-pointer"
                >
                  <option disabled value="">Location</option>
                  {locations.map((loc) => (
                    <option key={loc} value={loc}>{loc === "All" ? "Location" : loc}</option>
                  ))}
                </select>
                <div className="absolute right-4 pointer-events-none text-slate-500 text-xs">▼</div>
              </div>
            </div>
          </div>

          {/* Job Openings List */}
          <div className="space-y-4 mb-8">
            {filteredJobs.length > 0 ? (
              filteredJobs.map((job) => (
                <div 
                  key={job.id} 
                  className="p-6 md:p-8 bg-white border border-slate-100 rounded-2xl hover:border-slate-200 hover:shadow-lg hover:shadow-slate-100 transition-all duration-300 flex flex-col md:flex-row md:items-center justify-between gap-6 group"
                >
                  <div className="space-y-3">
                    <span className="inline-block text-xs font-bold tracking-wider text-slate-500 bg-slate-100 px-3 py-1 rounded-full uppercase">
                      {job.department}
                    </span>
                    <h3 className="text-xl md:text-2xl font-bold text-slate-900 group-hover:text-blue-600 transition-colors">
                      {job.title}
                    </h3>
                    <div className="flex items-center gap-4 text-sm text-slate-500">
                      <span className="flex items-center gap-1.5">
                        <MapPin className="w-4 h-4 text-slate-400" />
                        {job.location}
                      </span>
                      <span className="w-1.5 h-1.5 rounded-full bg-slate-300"></span>
                      <span className="flex items-center gap-1.5">
                        <Briefcase className="w-4 h-4 text-slate-400" />
                        {job.type}
                      </span>
                    </div>
                  </div>
                  
                  <button 
                    onClick={() => {
                      setSelectedJobTitle(job.title);
                      setIsApplyOpen(true);
                    }}
                    className="bg-[#0A66C2] hover:bg-blue-700 active:scale-98 text-white px-6 py-3 rounded-xl text-sm font-semibold transition-all whitespace-nowrap self-start md:self-auto shadow-md shadow-blue-500/5 cursor-pointer"
                  >
                    Apply Now
                  </button>
                </div>
              ))
            ) : (
              <div className="text-center py-12 bg-[#F8FAFC] rounded-2xl border border-dashed border-slate-200">
                <p className="text-slate-500 font-medium">No open positions found matching your criteria.</p>
              </div>
            )}
          </div>

          <div className="text-center">
            <button 
              onClick={() => {
                setSelectedJobTitle("General Application");
                setIsApplyOpen(true);
              }}
              className="inline-flex items-center gap-1.5 text-blue-600 hover:text-blue-700 font-semibold text-base transition-colors hover:underline cursor-pointer"
            >
              Send a general application
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </section>

      {/* VALUE & DEPTH SECTIONS */}
      <section id="culture" className="py-24 bg-[#F8FAFC]">
        <div className="max-w-7xl mx-auto px-6 space-y-24">
          
          {/* Section 1: Designed for Depth */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-6 max-w-xl">
              <h2 className="text-4xl sm:text-5xl font-bold tracking-tight text-slate-900 leading-tight">
                Designed for Depth
              </h2>
              <p className="text-slate-500 text-lg leading-relaxed">
                We believe that brilliance requires space. Our work culture is built around 'Deep Work' blocks, minimal meetings, and a radical focus on high-impact outcomes over administrative noise.
              </p>
              <div className="flex items-center gap-3 text-slate-700 font-semibold text-base">
                <div className="bg-emerald-50 text-emerald-600 p-1.5 rounded-full border border-emerald-100 flex items-center justify-center">
                  <Check className="w-5 h-5 stroke-[2.5]" />
                </div>
                4-Day Focused Work Week Option
              </div>
            </div>
            <div className="relative rounded-3xl overflow-hidden shadow-2xl">
              <img 
                src="/assets/modern_library.png" 
                alt="Modern quiet office workspace library" 
                className="w-full object-cover aspect-[16/10] hover:scale-103 transition-transform duration-700" 
              />
            </div>
          </div>

          {/* Section 2: Pioneering Ethics */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="relative rounded-3xl overflow-hidden shadow-2xl lg:order-first order-last">
              <img 
                src="/assets/ethics_lab.png" 
                alt="Scientific technology hardware researchers working in a lab" 
                className="w-full object-cover aspect-[16/10] hover:scale-103 transition-transform duration-700" 
              />
            </div>
            <div className="space-y-6 max-w-xl lg:pl-8">
              <h2 className="text-4xl sm:text-5xl font-bold tracking-tight text-slate-900 leading-tight">
                Pioneering Ethics
              </h2>
              <p className="text-slate-500 text-lg leading-relaxed">
                Innovation without ethics is mere motion. We bake responsibility into every line of code, ensuring that our advancements benefit humanity equitably and transparently.
              </p>
            </div>
          </div>

        </div>
      </section>

      {/* LIFE AT PRANAGA SECTION */}
      <section className="py-24 bg-white border-t border-slate-100">
        <div className="max-w-7xl mx-auto px-6">
          <div className="relative w-full rounded-3xl overflow-hidden shadow-2xl aspect-[4/3] bg-slate-100">
            <img 
              src={lifePhoto.src} 
              alt={lifePhoto.alt} 
              className="w-full h-full object-cover transition-all duration-500" 
            />
          </div>
        </div>
      </section>

      {/* HIRING PROCESS SECTION */}
      <section className="py-36 bg-[#0F172A] text-white relative overflow-hidden">
        {/* Background glow effects */}
        <div className="absolute top-1/2 -translate-y-1/2 -left-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div className="absolute top-1/2 -translate-y-1/2 -right-1/4 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div className="max-w-6xl mx-auto px-6 relative z-10">
          <div className="text-center max-w-2xl mx-auto mb-20">
            <h2 className="text-5xl lg:text-6xl font-extrabold tracking-[-0.04em] mb-6"></h2>
            <p className="text-slate-400 text-lg">
              Transparency starts with the first interview. Here's what to expect when you apply.
            </p>
          </div>

          {/* 4 Steps timeline */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 relative">
            {/* Connection Line */}
            <div className="hidden md:block absolute top-[45px] left-[10%] right-[10%] h-0.5 bg-slate-800 z-0"></div>

            {/* Step 1 */}
            <div className="flex flex-col items-center text-center group z-10">
              <div className="w-[90px] h-[90px] rounded-full bg-blue-600 flex items-center justify-center text-white mb-6 border-4 border-slate-950 shadow-xl group-hover:scale-105 transition-all">
                <Send className="w-8 h-8 stroke-[1.5]" />
              </div>
              <h3 className="text-xl font-bold mb-3">1. Apply</h3>
              <p className="text-slate-400 text-sm leading-relaxed max-w-[220px]">
                Submit your application. Our recruiters will review every profile.
              </p>
            </div>

            {/* Step 2 */}
            <div className="flex flex-col items-center text-center group z-10">
              <div className="w-[90px] h-[90px] rounded-full bg-[#0E56A8] flex items-center justify-center text-white mb-6 border-4 border-slate-950 shadow-xl group-hover:scale-105 transition-all">
                <Phone className="w-8 h-8 stroke-[1.5]" />
              </div>
              <h3 className="text-xl font-bold mb-3">2. Screen</h3>
              <p className="text-slate-400 text-sm leading-relaxed max-w-[220px]">
                A 30-minute introductory call to discuss your experience and goals.
              </p>
            </div>

            {/* Step 3 */}
            <div className="flex flex-col items-center text-center group z-10">
              <div className="w-[90px] h-[90px] rounded-full bg-[#0C4CA3] flex items-center justify-center text-white mb-6 border-4 border-slate-950 shadow-xl group-hover:scale-105 transition-all">
                <MessageSquare className="w-8 h-8 stroke-[1.5]" />
              </div>
              <h3 className="text-xl font-bold mb-3">3. Interview</h3>
              <p className="text-slate-400 text-sm leading-relaxed max-w-[220px]">
                Meet the team. We focus on real-world problem solving and collaboration.
              </p>
            </div>

            {/* Step 4 */}
            <div className="flex flex-col items-center text-center group z-10">
              <div className="w-[90px] h-[90px] rounded-full bg-blue-600 flex items-center justify-center text-white mb-6 border-4 border-slate-950 shadow-xl group-hover:scale-105 transition-all">
                <Award className="w-8 h-8 stroke-[1.5]" />
              </div>
              <h3 className="text-xl font-bold mb-3">4. Offer</h3>
              <p className="text-slate-400 text-sm leading-relaxed max-w-[220px]">
                The final step. Welcome to the team that's building the future of AI.
              </p>
            </div>

          </div>
        </div>
      </section>

      {/* HOLISTIC EMPOWERMENT (BENEFITS) */}
      <section className="py-24 bg-[#F8FAFC]">
        <div className="max-w-5xl mx-auto px-6">
          <div className="text-center max-w-2xl mx-auto mb-16">
            <h2 className="text-4xl font-bold tracking-tight text-slate-900 mb-4">
              Holistic Empowerment
            </h2>
            <p className="text-slate-500 text-lg">
              We provide the foundation you need to thrive personally and professionally.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            
            {/* Any Time Benefit */}
            <div className="p-12 bg-white border border-slate-100 rounded-3xl shadow-sm flex flex-col items-center text-center group hover:shadow-lg transition-shadow">
              <div className="w-14 h-14 bg-[#F8FAFC] text-slate-700 rounded-full flex items-center justify-center border border-slate-150 mb-6">
                <ShieldAlert className="w-6 h-6 stroke-[1.8]" />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Any Time</h3>
              <p className="text-slate-500 leading-relaxed max-w-[280px]">
                Work in your free time
              </p>
            </div>

            {/* Work Anywhere Benefit */}
            <div className="p-12 bg-white border border-slate-100 rounded-3xl shadow-sm flex flex-col items-center text-center group hover:shadow-lg transition-shadow">
              <div className="w-14 h-14 bg-[#F8FAFC] text-slate-700 rounded-full flex items-center justify-center border border-slate-150 mb-6">
                <MapPin className="w-6 h-6 stroke-[1.8]" />
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">Work Anywhere</h3>
              <p className="text-slate-500 leading-relaxed max-w-[340px]">
                Flexible remote-first infrastructure with luxury coworking passes and home office stipends.
              </p>
            </div>

          </div>
        </div>
      </section>

      {/* VOICE OF THE TEAM (TESTIMONIALS) */}
      <section id="testimonials" className="py-24 bg-white border-t border-slate-100 overflow-hidden">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-6 mb-16">
            <div className="space-y-4">
              <h2 className="text-4xl sm:text-5xl font-bold tracking-tight text-slate-900">
                Voice of the Team
              </h2>
            </div>
            
            <div className="flex items-center gap-3">
              <button 
                onClick={handlePrevTestimonial}
                className="w-12 h-12 rounded-full border border-slate-200 hover:border-slate-400 hover:bg-slate-50 active:scale-95 flex items-center justify-center transition-all cursor-pointer"
              >
                <ChevronLeft className="w-5 h-5 text-slate-700" />
              </button>
              <button 
                onClick={handleNextTestimonial}
                className="w-12 h-12 rounded-full border border-slate-200 hover:border-slate-400 hover:bg-slate-50 active:scale-95 flex items-center justify-center transition-all cursor-pointer"
              >
                <ChevronRight className="w-5 h-5 text-slate-700" />
              </button>
            </div>
          </div>

          <div className="overflow-hidden w-full py-4">
            <style>{`
              .testimonials-track {
                transform: translateX(-${activeTestimonial * 100}%);
              }
              @media (min-width: 768px) {
                .testimonials-track {
                  transform: translateX(${-(activeTestimonial - 1) * 33.333}%);
                }
              }
            `}</style>
            <div className="flex transition-transform duration-500 ease-in-out testimonials-track">
              {sliderTestimonials.map((testimonial, idx) => {
                const isMiddle = idx === activeTestimonial + 1;
                return (
                  <div 
                    key={`${testimonial.id}-${idx}`}
                    className="w-full md:w-1/3 shrink-0 px-4 transition-all duration-500"
                  >
                    <div 
                      className={`p-8 bg-white border rounded-3xl flex flex-col justify-between gap-8 h-full transition-all duration-500 ${
                        isMiddle 
                          ? "border-blue-500 ring-4 ring-blue-500/10 shadow-2xl scale-105 z-10 opacity-100" 
                          : "border-slate-100 scale-95 opacity-60 z-0"
                      } ${
                        testimonial.id === "t1" ? "border-l-[6px] border-l-[#8A2BE2]" : ""
                      }`}
                    >
                      <p className="text-slate-700 text-base leading-relaxed italic">
                        "{testimonial.quote}"
                      </p>
                      
                      <div className="flex items-center gap-4">
                        <img 
                          src={testimonial.avatar} 
                          alt={testimonial.author} 
                          className="w-12 h-12 rounded-full object-cover border border-slate-200"
                        />
                        <div className="space-y-0.5">
                          <h4 className="font-bold text-slate-900 text-sm">
                            {testimonial.author}
                          </h4>
                          <p className="text-[11px] font-bold text-slate-400 uppercase tracking-wider">
                            {testimonial.role}
                          </p>
                        </div>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </section>

      {/* READY TO JOIN US BANNER */}
      <section className="py-12 bg-white">
        <div className="max-w-7xl mx-auto px-6">
          <div className="bg-[#0A66C2] rounded-[32px] p-12 md:p-20 text-center relative overflow-hidden shadow-2xl">
            {/* Decorative circles */}
            <div className="absolute top-1/2 -translate-y-1/2 -right-12 w-64 h-64 bg-white/5 rounded-full border border-white/10 pointer-events-none"></div>
            <div className="absolute top-1/2 -translate-y-1/2 -right-24 w-80 h-80 bg-white/5 rounded-full border border-white/10 pointer-events-none"></div>
            
            <div className="relative z-10 max-w-xl mx-auto space-y-8">
              <h2 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-white leading-none">
                Ready to join Us
              </h2>
              
              <div className="flex flex-col sm:flex-row justify-center gap-4">
                <a 
                  href="#openings" 
                  className="bg-white hover:bg-slate-50 text-blue-700 font-semibold px-8 py-4 rounded-xl text-base transition-all active:scale-98 shadow-lg shadow-black/5"
                >
                  Explore Opportunities
                </a>
                <button 
                  onClick={() => {
                    setSelectedJobTitle("Talk to Recruiter");
                    setIsApplyOpen(true);
                  }}
                  className="bg-[#1875D3] hover:bg-[#1E83EC] border border-[#2D8BEF] text-white font-semibold px-8 py-4 rounded-xl text-base transition-all active:scale-98 cursor-pointer"
                >
                  Talk to a Recruiter
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-white pt-24 pb-12 border-t border-slate-100">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-12 gap-12 md:gap-8 pb-16">
            
            {/* Brand column */}
            <div className="md:col-span-4 space-y-6">
              <h3 className="text-2xl font-bold tracking-tight text-blue-600">Pranaga</h3>
              <p className="text-slate-500 text-sm leading-relaxed max-w-xs">
                Redefining team collaboration through the power of generative intelligence and executive-level precision.
              </p>
              
              {/* Social icons */}
              <div className="flex items-center gap-3">
                <a href="#globe" onClick={() => alert("Navigating to Pranaga Main Website...")} className="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-blue-50 hover:text-blue-600 hover:border-blue-100 transition-all text-slate-500">
                  <Globe className="w-5 h-5" />
                </a>
                <a href="#chat" onClick={() => setIsChatOpen(true)} className="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-blue-50 hover:text-blue-600 hover:border-blue-100 transition-all text-slate-500">
                  <MessageCircle className="w-5 h-5" />
                </a>
                <a href="#openings" className="w-10 h-10 rounded-full bg-slate-50 border border-slate-100 flex items-center justify-center hover:bg-blue-50 hover:text-blue-600 hover:border-blue-100 transition-all text-slate-500">
                  <Briefcase className="w-5 h-5" />
                </a>
              </div>
            </div>

            {/* Links columns */}
            <div className="md:col-span-8 grid grid-cols-2 sm:grid-cols-4 gap-8">
              
              {/* Product */}
              <div className="space-y-4">
                <h4 className="text-xs font-bold text-slate-900 uppercase tracking-widest">Product</h4>
                <ul className="space-y-3 text-sm font-medium text-slate-500">
                  <li><a href="#dashboard" onClick={() => alert("Navigating to Dashboard...")} className="hover:text-slate-950 transition-colors">Dashboard</a></li>
                  <li><a href="#task-engine" onClick={() => alert("Navigating to Task Engine...")} className="hover:text-slate-950 transition-colors">Task Engine</a></li>
                  <li><a href="#ai-copilot" onClick={() => alert("Navigating to AI Copilot...")} className="hover:text-slate-950 transition-colors">AI Copilot</a></li>
                  <li><a href="#integrations" onClick={() => alert("Navigating to Integrations...")} className="hover:text-slate-950 transition-colors">Integrations</a></li>
                </ul>
              </div>

              {/* Company */}
              <div className="space-y-4">
                <h4 className="text-xs font-bold text-slate-900 uppercase tracking-widest">Company</h4>
                <ul className="space-y-3 text-sm font-medium text-slate-500">
                  <li><a href="#about" onClick={() => alert("Navigating to About Us...")} className="hover:text-slate-950 transition-colors">About Us</a></li>
                  <li><a href="#openings" className="text-[#0A66C2] font-semibold hover:opacity-90">Careers</a></li>
                  <li><a href="#culture" className="hover:text-slate-950 transition-colors">Culture</a></li>
                  <li><a href="#press" onClick={() => alert("Navigating to Press Kit...")} className="hover:text-slate-950 transition-colors">Press Kit</a></li>
                </ul>
              </div>

              {/* Resources */}
              <div className="space-y-4">
                <h4 className="text-xs font-bold text-slate-900 uppercase tracking-widest">Resources</h4>
                <ul className="space-y-3 text-sm font-medium text-slate-500">
                  <li><a href="#help" onClick={() => alert("Navigating to Help Center...")} className="hover:text-slate-950 transition-colors">Help Center</a></li>
                  <li><a href="#guides" onClick={() => alert("Navigating to Guides...")} className="hover:text-slate-950 transition-colors">Guides</a></li>
                  <li><a href="#docs" onClick={() => alert("Navigating to API Docs...")} className="hover:text-slate-950 transition-colors">API Docs</a></li>
                  <li><a href="#pricing" onClick={() => alert("Navigating to Pricing...")} className="hover:text-slate-950 transition-colors">Pricing</a></li>
                </ul>
              </div>

              {/* Legal */}
              <div className="space-y-4">
                <h4 className="text-xs font-bold text-slate-900 uppercase tracking-widest">Legal</h4>
                <ul className="space-y-3 text-sm font-medium text-slate-500">
                  <li><a href="#privacy" onClick={() => alert("Navigating to Privacy Policy...")} className="hover:text-slate-950 transition-colors">Privacy Policy</a></li>
                  <li><a href="#terms" onClick={() => alert("Navigating to Terms of Service...")} className="hover:text-slate-950 transition-colors">Terms of Service</a></li>
                  <li><a href="#security" onClick={() => alert("Navigating to Security Policy...")} className="hover:text-slate-950 transition-colors">Security</a></li>
                </ul>
              </div>

            </div>

          </div>

          {/* Copyright bar */}
          <div className="pt-8 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <p className="text-slate-400 text-xs font-medium">
              © 2024 Pranaga AI Enterprise Workspace. All rights reserved.
            </p>
            <div className="flex items-center gap-6 text-slate-400 text-xs font-medium">
              <button onClick={() => setIsCookieOpen(true)} className="hover:text-slate-600 transition-colors cursor-pointer">Cookie Settings</button>
              <button onClick={() => setIsAccessibilityOpen(true)} className="hover:text-slate-600 transition-colors cursor-pointer">Accessibility</button>
            </div>
          </div>

        </div>
      </footer>

      {/* CONTACT FORM MODAL */}
      {isContactOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4">
          <div className="bg-white w-full max-w-lg rounded-3xl p-8 border border-slate-100 shadow-2xl animate-fade-in relative">
            <button 
              onClick={() => setIsContactOpen(false)}
              className="absolute top-6 right-6 text-slate-400 hover:text-slate-600 transition-colors p-1"
            >
              <X className="w-6 h-6" />
            </button>

            <h3 className="text-2xl font-bold text-slate-900 mb-2">Get in touch</h3>
            <p className="text-slate-500 mb-6">Drop us a line and our team will get back to you shortly.</p>

            {contactSuccess ? (
              <div className="py-12 flex flex-col items-center justify-center text-center space-y-4">
                <div className="w-16 h-16 bg-emerald-50 text-emerald-600 rounded-full flex items-center justify-center border border-emerald-100">
                  <Check className="w-8 h-8 stroke-[2.5]" />
                </div>
                <h4 className="text-lg font-bold text-slate-900">Message sent!</h4>
                <p className="text-slate-500 text-sm">Thank you for reaching out. We will contact you soon.</p>
              </div>
            ) : (
              <form onSubmit={handleContactSubmit} className="space-y-5">
                <div className="space-y-1.5">
                  <label className="text-sm font-bold text-slate-800 flex items-center gap-1.5">
                    <User className="w-4 h-4 text-slate-400" /> Name
                  </label>
                  <input 
                    type="text" 
                    required
                    placeholder="Jane Doe"
                    value={contactName}
                    onChange={(e) => setContactName(e.target.value)}
                    className="w-full px-4 py-3 bg-[#F1F3F5] rounded-xl focus:outline-none focus:bg-white focus:ring-2 focus:ring-blue-500/10 focus:border-blue-500 border border-transparent text-[15px] transition-all placeholder:text-slate-400"
                  />
                </div>

                <div className="space-y-1.5">
                  <label className="text-sm font-bold text-slate-800 flex items-center gap-1.5">
                    <Mail className="w-4 h-4 text-slate-400" /> Email Address
                  </label>
                  <input 
                    type="email" 
                    required
                    placeholder="jane@company.com"
                    value={contactEmail}
                    onChange={(e) => setContactEmail(e.target.value)}
                    className="w-full px-4 py-3 bg-[#F1F3F5] rounded-xl focus:outline-none focus:bg-white focus:ring-2 focus:ring-blue-500/10 focus:border-blue-500 border border-transparent text-[15px] transition-all placeholder:text-slate-400"
                  />
                </div>

                <div className="space-y-1.5">
                  <label className="text-sm font-bold text-slate-800 flex items-center gap-1.5">
                    <MessageSquareDiff className="w-4 h-4 text-slate-400" /> Message
                  </label>
                  <textarea 
                    required
                    rows={4}
                    placeholder="How can we help you?"
                    value={contactMessage}
                    onChange={(e) => setContactMessage(e.target.value)}
                    className="w-full px-4 py-3 bg-[#F1F3F5] rounded-xl focus:outline-none focus:bg-white focus:ring-2 focus:ring-blue-500/10 focus:border-blue-500 border border-transparent text-[15px] transition-all placeholder:text-slate-400 resize-none"
                  />
                </div>

                <button 
                  type="submit"
                  className="w-full bg-[#0A66C2] hover:bg-blue-700 text-white font-semibold py-3.5 rounded-xl shadow-lg shadow-blue-500/5 transition-all text-center cursor-pointer active:scale-98"
                >
                  Send Message
                </button>
              </form>
            )}
          </div>
        </div>
      )}

      {/* JOB APPLICATION MODAL */}
      {isApplyOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4">
          <div className="bg-white w-full max-w-lg rounded-3xl p-8 border border-slate-100 shadow-2xl animate-fade-in relative">
            <button 
              onClick={() => setIsApplyOpen(false)}
              className="absolute top-6 right-6 text-slate-400 hover:text-slate-600 transition-colors p-1"
            >
              <X className="w-6 h-6" />
            </button>

            <span className="inline-block text-[11px] font-bold tracking-wider text-blue-600 bg-blue-50 px-3 py-1 rounded-full uppercase mb-2">
              Apply Now
            </span>
            <h3 className="text-2xl font-bold text-slate-900 mb-1">{selectedJobTitle}</h3>
            <p className="text-slate-500 mb-6">Pranaga AI Workspace Integration Team</p>

            {applySuccess ? (
              <div className="py-12 flex flex-col items-center justify-center text-center space-y-4">
                <div className="w-16 h-16 bg-emerald-50 text-emerald-600 rounded-full flex items-center justify-center border border-emerald-100">
                  <Check className="w-8 h-8 stroke-[2.5]" />
                </div>
                <h4 className="text-lg font-bold text-slate-900">Application Submitted!</h4>
                <p className="text-slate-500 text-sm">Thanks for applying. Our recruiting team will review your profile shortly.</p>
              </div>
            ) : (
              <form onSubmit={handleApplySubmit} className="space-y-5">
                <div className="space-y-1.5">
                  <label className="text-sm font-bold text-slate-800 flex items-center gap-1.5">
                    <User className="w-4 h-4 text-slate-400" /> Full Name
                  </label>
                  <input 
                    type="text" 
                    required
                    placeholder="Jane Doe"
                    value={applyName}
                    onChange={(e) => setApplyName(e.target.value)}
                    className="w-full px-4 py-3 bg-[#F1F3F5] rounded-xl focus:outline-none focus:bg-white focus:ring-2 focus:ring-blue-500/10 focus:border-blue-500 border border-transparent text-[15px] transition-all placeholder:text-slate-400"
                  />
                </div>

                <div className="space-y-1.5">
                  <label className="text-sm font-bold text-slate-800 flex items-center gap-1.5">
                    <Mail className="w-4 h-4 text-slate-400" /> Email Address
                  </label>
                  <input 
                    type="email" 
                    required
                    placeholder="jane@example.com"
                    value={applyEmail}
                    onChange={(e) => setApplyEmail(e.target.value)}
                    className="w-full px-4 py-3 bg-[#F1F3F5] rounded-xl focus:outline-none focus:bg-white focus:ring-2 focus:ring-blue-500/10 focus:border-blue-500 border border-transparent text-[15px] transition-all placeholder:text-slate-400"
                  />
                </div>

                <div className="space-y-1.5">
                  <label className="text-sm font-bold text-slate-800 flex items-center gap-1.5">
                    <Globe className="w-4 h-4 text-slate-400" /> Portfolio / LinkedIn URL
                  </label>
                  <input 
                    type="url" 
                    placeholder="https://linkedin.com/in/username"
                    value={applyPortfolio}
                    onChange={(e) => setApplyPortfolio(e.target.value)}
                    className="w-full px-4 py-3 bg-[#F1F3F5] rounded-xl focus:outline-none focus:bg-white focus:ring-2 focus:ring-blue-500/10 focus:border-blue-500 border border-transparent text-[15px] transition-all placeholder:text-slate-400"
                  />
                </div>

                <div className="space-y-1.5">
                  <label className="text-sm font-bold text-slate-800 flex items-center gap-1.5">
                    <FileText className="w-4 h-4 text-slate-400" /> Resume / CV
                  </label>
                  <div className="border-2 border-dashed border-slate-200 rounded-xl p-6 text-center hover:bg-slate-50 transition-colors relative cursor-pointer group">
                    <input 
                      type="file"
                      required
                      onChange={(e) => {
                        if (e.target.files && e.target.files[0]) {
                          setApplyFileName(e.target.files[0].name);
                        }
                      }}
                      className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                    />
                    <FileText className="w-8 h-8 text-slate-400 mx-auto mb-2 group-hover:text-blue-600 transition-colors" />
                    <p className="text-sm font-bold text-slate-800 mb-0.5">
                      {applyFileName || "Click to upload resume"}
                    </p>
                    <p className="text-xs text-slate-400">PDF, DOCX up to 10MB</p>
                  </div>
                </div>

                <button 
                  type="submit"
                  className="w-full bg-[#0A66C2] hover:bg-blue-700 text-white font-semibold py-3.5 rounded-xl shadow-lg shadow-blue-500/5 transition-all text-center cursor-pointer active:scale-98"
                >
                  Submit Application
                </button>
              </form>
            )}
          </div>
        </div>
      )}

      {/* COOKIE SETTINGS MODAL */}
      {isCookieOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4">
          <div className="bg-white w-full max-w-md rounded-3xl p-8 border border-slate-100 shadow-2xl animate-fade-in relative">
            <button 
              onClick={() => setIsCookieOpen(false)}
              className="absolute top-6 right-6 text-slate-400 hover:text-slate-600 transition-colors p-1"
            >
              <X className="w-6 h-6" />
            </button>

            <h3 className="text-xl font-bold text-slate-900 mb-3 flex items-center gap-2">
              <ShieldAlert className="w-6 h-6 text-blue-600" />
              Cookie Preferences
            </h3>
            <p className="text-slate-500 text-sm leading-relaxed mb-6">
              We use cookies to optimize site performance, analyze website traffic, and support marketing initiatives. You can configure your preferences below.
            </p>

            <div className="space-y-4 mb-6">
              <div className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-100">
                <div>
                  <h4 className="font-bold text-slate-900 text-sm">Essential Cookies</h4>
                  <p className="text-[11px] text-slate-400">Required for website features. Cannot be disabled.</p>
                </div>
                <div className="text-xs font-bold text-blue-600 bg-blue-50 px-2 py-1 rounded">ALWAYS ON</div>
              </div>

              <div className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-100">
                <div>
                  <h4 className="font-bold text-slate-900 text-sm">Analytical Cookies</h4>
                  <p className="text-[11px] text-slate-400">Helps us track and improve website performance.</p>
                </div>
                <input type="checkbox" defaultChecked className="w-5 h-5 accent-blue-600 cursor-pointer" />
              </div>
            </div>

            <button 
              onClick={() => setIsCookieOpen(false)}
              className="w-full bg-[#0A66C2] hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition-all cursor-pointer text-center"
            >
              Save Settings
            </button>
          </div>
        </div>
      )}

      {/* ACCESSIBILITY MODAL */}
      {isAccessibilityOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4">
          <div className="bg-white w-full max-w-md rounded-3xl p-8 border border-slate-100 shadow-2xl animate-fade-in relative">
            <button 
              onClick={() => setIsAccessibilityOpen(false)}
              className="absolute top-6 right-6 text-slate-400 hover:text-slate-600 transition-colors p-1"
            >
              <X className="w-6 h-6" />
            </button>

            <h3 className="text-xl font-bold text-slate-900 mb-3 flex items-center gap-2">
              <Info className="w-6 h-6 text-blue-600" />
              Accessibility Features
            </h3>
            <p className="text-slate-500 text-sm leading-relaxed mb-6">
              Our website is built using WCAG 2.1 accessibility standards to support screen readers, keyboard navigation, and custom readability preferences.
            </p>

            <div className="space-y-4 mb-6">
              <div className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-100">
                <div>
                  <h4 className="font-bold text-slate-900 text-sm">Increase Contrast</h4>
                  <p className="text-[11px] text-slate-400">Improves readability for visual impairments.</p>
                </div>
                <input type="checkbox" className="w-5 h-5 accent-blue-600 cursor-pointer" />
              </div>

              <div className="flex items-center justify-between p-3 bg-slate-50 rounded-xl border border-slate-100">
                <div>
                  <h4 className="font-bold text-slate-900 text-sm">Keyboard Guidelines</h4>
                  <p className="text-[11px] text-slate-400">Shows focus indicators during tab index selection.</p>
                </div>
                <input type="checkbox" defaultChecked className="w-5 h-5 accent-blue-600 cursor-pointer" />
              </div>
            </div>

            <button 
              onClick={() => setIsAccessibilityOpen(false)}
              className="w-full bg-[#0A66C2] hover:bg-blue-700 text-white font-semibold py-3 rounded-xl transition-all cursor-pointer text-center"
            >
              Close Guidelines
            </button>
          </div>
        </div>
      )}

      {/* FLOATING AI ASSISTANT ROBOT BUTTON */}
      <button
        onClick={() => setIsChatOpen((prev) => !prev)}
        title="AI Assistant"
        className="fixed bottom-6 right-6 z-50 w-16 h-16 rounded-full bg-[#0A66C2] hover:bg-blue-700 active:scale-95 text-white shadow-xl shadow-blue-500/30 flex items-center justify-center transition-all duration-200 hover:shadow-2xl hover:shadow-blue-500/40 cursor-pointer"
        style={{ display: isChatOpen ? 'none' : 'flex' }}
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" className="w-8 h-8">
          <rect x="3" y="11" width="18" height="11" rx="2" />
          <path d="M12 2a2 2 0 0 1 2 2v1H10V4a2 2 0 0 1 2-2z" />
          <line x1="12" y1="5" x2="12" y2="11" />
          <circle cx="9" cy="16" r="1.2" fill="currentColor" stroke="none" />
          <circle cx="15" cy="16" r="1.2" fill="currentColor" stroke="none" />
          <path d="M9 19.5c1-1 5-1 6 0" />
          <line x1="6" y1="14" x2="4" y2="14" />
          <line x1="18" y1="14" x2="20" y2="14" />
        </svg>
      </button>

      {/* CHAT WIDGET OVERLAY */}
      {isChatOpen && (
        <div className="fixed bottom-6 right-6 z-50 w-full max-w-[380px] bg-white rounded-3xl border border-slate-100 shadow-2xl flex flex-col overflow-hidden animate-fade-in">
          {/* Chat Header */}
          <div className="bg-[#0A66C2] p-5 text-white flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center font-bold text-sm">P</div>
              <div>
                <h4 className="font-bold text-sm">Pranaga Assistant</h4>
                <p className="text-[10px] text-blue-200">Online | AI Copilot</p>
              </div>
            </div>
            <button 
              onClick={() => setIsChatOpen(false)}
              className="text-white/80 hover:text-white transition-colors p-1"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Messages History */}
          <div className="flex-1 h-80 overflow-y-auto p-4 space-y-3 bg-[#F8FAFC]">
            {chatMessages.map((msg, index) => (
              <div 
                key={index}
                className={`max-w-[85%] rounded-2xl px-4 py-2.5 text-[13px] leading-relaxed ${
                  msg.sender === "user" 
                    ? "bg-[#0A66C2] text-white ml-auto rounded-tr-none" 
                    : "bg-white text-slate-800 border border-slate-100 mr-auto rounded-tl-none shadow-sm"
                }`}
              >
                {msg.text}
              </div>
            ))}
            {isBotTyping && (
              <div className="bg-white text-slate-500 border border-slate-100 rounded-2xl rounded-tl-none px-4 py-2.5 text-xs mr-auto shadow-sm max-w-[85%] flex items-center gap-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce"></span>
                <span className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce [animation-delay:0.2s]"></span>
                <span className="w-1.5 h-1.5 rounded-full bg-slate-400 animate-bounce [animation-delay:0.4s]"></span>
              </div>
            )}
            <div ref={chatEndRef} />
          </div>

          {/* Quick Prompts */}
          <div className="p-3 bg-white border-t border-slate-100 flex flex-wrap gap-1.5">
            <button 
              onClick={() => handleSendChatMessage("What benefits do you offer?")}
              className="text-[11px] font-semibold text-blue-600 bg-blue-50 border border-blue-100 hover:bg-blue-100 px-2.5 py-1 rounded-full transition-colors cursor-pointer"
            >
              Benefits
            </button>
            <button 
              onClick={() => handleSendChatMessage("Tell me about the culture.")}
              className="text-[11px] font-semibold text-blue-600 bg-blue-50 border border-blue-100 hover:bg-blue-100 px-2.5 py-1 rounded-full transition-colors cursor-pointer"
            >
              Culture
            </button>
            <button 
              onClick={() => handleSendChatMessage("How does the interview process work?")}
              className="text-[11px] font-semibold text-blue-600 bg-blue-50 border border-blue-100 hover:bg-blue-100 px-2.5 py-1 rounded-full transition-colors cursor-pointer"
            >
              Interview Process
            </button>
            <button 
              onClick={() => handleSendChatMessage("What job roles are open?")}
              className="text-[11px] font-semibold text-blue-600 bg-blue-50 border border-blue-100 hover:bg-blue-100 px-2.5 py-1 rounded-full transition-colors cursor-pointer"
            >
              Job Openings
            </button>
          </div>

          {/* Message Input Box */}
          <form 
            onSubmit={(e) => {
              e.preventDefault();
              handleSendChatMessage(chatInput);
            }}
            className="p-3 bg-white border-t border-slate-100 flex gap-2"
          >
            <input 
              type="text"
              placeholder="Ask a question..."
              value={chatInput}
              onChange={(e) => setChatInput(e.target.value)}
              className="flex-1 px-3 py-2 bg-slate-50 border border-slate-150 rounded-xl focus:outline-none focus:bg-white text-xs"
            />
            <button 
              type="submit"
              className="bg-[#0A66C2] hover:bg-blue-700 text-white p-2.5 rounded-xl flex items-center justify-center transition-colors cursor-pointer"
            >
              <Send className="w-3.5 h-3.5" />
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default Careers;